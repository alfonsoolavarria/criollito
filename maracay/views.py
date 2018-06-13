from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View, TemplateView
from django.contrib.sessions.models import Session
from maracay.backEnd import backStart, profileBackend
from django.shortcuts import render
from django.core.cache import cache
from maracay import get_client_ip
import json


# Create your views here.
#Main Class
class Maracay(TemplateView):
    template_name = 'market/index.html'
    #index
    def get(self, request, *args, **kwargs):
        _allproducts = backStart(request)
        _allproducts.get('all')
        data = _allproducts.response_data
        data['code'] = _allproducts.code
        return render(request, 'market/index.html',{'data':data['data'][0]})

class Account(View):
    def get(self, request, *args, **kwargs):
        if str(request.user) != 'AnonymousUser':#si esta logeado su data
            return render(request, 'market/account.html', {})
        else: # registro
            return render(request, 'market/register.html', {})


class Login(View):
    def __init__(self):
        self.requireds = ['email', 'password', 'csrfmiddlewaretoken']

    def post(self, request, *args, **kwargs):
        __ip = get_client_ip(request)

        for key in self.requireds:
            if not key in request.POST.keys():
                return HttpResponse(status=400, content_type='application/json')
        for session in Session.objects.filter(session_key=request.session.session_key):
            if session:
                #No se puede iniciar Sesion usuario ya tiene una sesion activa
                return HttpResponse(json.dumps({'code':400}, cls=DjangoJSONEncoder), content_type='application/json')

        if cache.get('cache_ip__%s'%__ip):
            return HttpResponse(json.dumps({'code':400,'message':'Debe esperar 5 minutos'}, cls=DjangoJSONEncoder), content_type='application/json')

        user = authenticate(username=request.POST['email'], password=request.POST['password'])

        if user:
            login(request, user)
            return HttpResponse(json.dumps({'code':200}, cls=DjangoJSONEncoder), content_type='application/json')
        else:

            __cache_count_error = cache.get('cache_error__%s'%__ip)
            __cache_exist = cache.get('cache_ip__%s'%__ip)

            if __cache_exist:
                print ("primeroooo 5 minutoss")
                return HttpResponse(json.dumps({'code':400,'message':'Debe esperar 5 minutos'}, cls=DjangoJSONEncoder), content_type='application/json')
            else:
                if __cache_count_error:
                    if __cache_count_error == 1:
                        cache.set('cache_error__%s'%__ip,1+1,60)
                        return HttpResponse(json.dumps({'code':400,'message':'Segundo intento fallido'}, cls=DjangoJSONEncoder), content_type='application/json')
                    elif __cache_count_error == 2:
                        cache.set('cache_ip__%s'%__ip,__ip,300)
                        return HttpResponse(json.dumps({'code':400,'message':'Tercer intento fallido/Debe esperar 5 minutos'}, cls=DjangoJSONEncoder), content_type='application/json')
                else:
                    cache.set('cache_error__%s'%__ip,1,60)
                    return HttpResponse(json.dumps({'code':400,'message':'Primer intento fallido'}, cls=DjangoJSONEncoder), content_type='application/json')

class Logout(View):
    def get(self, request, *args, **kwargs):
        logout(request)

        _allproducts = backStart(request)
        _allproducts.get('all')
        data = _allproducts.response_data
        data['code'] = _allproducts.code
        return render(request, 'market/index.html',{'data':data['data'][0]})


class Profile(View):
    def get(self, request, *args, **kwargs):
        print ("Profile")

    #creacion de usuarios
    def post(self, request, *args, **kwargs):
        _newUser = profileBackend(request)
        _newUser.post()
        data = _newUser.response_data
        data['code'] = _newUser.code
        user = authenticate(username=request.POST['email'], password=request.POST['password'])
        if user:login(request, user)
        return HttpResponse(json.dumps(data, cls=DjangoJSONEncoder), content_type='application/json')


def Conditions(request):
    return render(request, 'market/conditions.html', {})

def Help(request):
    return render(request, 'market/help.html', {})

def We(request):
    return render(request, 'market/we.html', {})

def Places(request):
    return render(request, 'market/places.html', {})

def Payment(request):
    return render(request, 'market/payment.html', {})

def Delivery(request):
    return render(request, 'market/delivery.html', {})
