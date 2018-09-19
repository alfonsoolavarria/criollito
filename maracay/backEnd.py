from django.contrib.auth.models import User
from maracay.models import Products, Profile
from django.db import transaction



class backStart():
    def __init__(self, request):
        self._request = request
        self.user = 0
        self.response_data = {'error':[], 'data':[],'data2':[]}
        self.code = 200

    def get(self,params=None):
        self.response_data['cantTotal']= Products.objects.all()
        #self.response_data['first'] = self._request.GET.get('start',0)
        #self.response_data['last'] = self._request.GET.get('end',12)

        try:
            for a in Products.objects.all():
                self.response_data['data'].append({
                "category":a.category,
                "id":a.id,
                "name":a.name,
                "cant":a.cant,
                "description":a.description,
                "image":a.image,
                #"price":a.price,
                })
            '''for b in Products.objects.filter()[int(self._request.GET.get('start',0)):int(self._request.GET.get('end',12))]:
                self.response_data['data2'].append({
                "category":b.category,
                "id":b.id,
                "cant":b.cant,
                "name":b.name,
                "description":b.description,
                "image":b.image,
                #"price":b.price,
                })'''
        except Exception as e:
            self.code = 500
            return self.response_data['error'].append(str(e))



class profileBackend():
    def __init__(self, request):
        self._request = request
        self.user = 0
        self.response_data = {'error':[], 'data':[]}
        self.code = 200

    def post(self):
        #creacion de Usuario
        inssertDict = {}
        inssertDictProfile = {}
        if 'email' in self._request.POST:
            inssertDict['email'] = self._request.POST['email']
            inssertDict['username'] = self._request.POST['email']
        else:
            return self.response_data['error'].append("Error al crear Usuario/Sin email")

        if 'password' in self._request.POST:
            inssertDict['password'] = self._request.POST['password']
        else:
            return self.response_data['error'].append("Error al crear Usuario/Sin contraseña")

        if 'phone' in self._request.POST:
            inssertDictProfile['phone'] = self._request.POST['phone']
        else:
            return self.response_data['error'].append("Debe insertar un número célular")

        if 'direction' in self._request.POST:
            inssertDictProfile['direction'] = self._request.POST['direction']
        else:
            return self.response_data['error'].append("Debe insertar una Dirección")

        if 'Tw' in self._request.POST:
            inssertDictProfile['tw'] = self._request.POST['Tw']
        else:
            inssertDictProfile['tw'] = ''

        if 'Fb' in self._request.POST:
            inssertDictProfile['fb'] = self._request.POST['Fb']
        else:
            inssertDictProfile['fb'] = ''

        if 'Goo' in self._request.POST:
            inssertDictProfile['google'] = self._request.POST['Goo']
        else:
            inssertDictProfile['google'] = ''

        try:
            with transaction.atomic():
                try:
                    getVerifiedUser = User.objects.get(username=inssertDict['username'])
                    self.code = 500
                    return self.response_data['error'].append("Ya este Email existe")
                except Exception as e:
                    user = User.objects.create_user(**inssertDict)
                    inssertDictProfile['user'] = user
                    creteProfile = Profile(**inssertDictProfile)
                    creteProfile.save()
        except Exception as e:
            print (e)
            self.code = 500
            return self.response_data['error'].append("Error al crear Usuario"+str(e))


class filterProducts():
    def __init__(self, request):
        self._request = request
        self.user = 0
        self.response_data = {'error':[], 'data':[]}
        self.code = 200

    def allProductsFilter(self):
        self.response_data['cantTotal']= Products.objects.all()
        for a in Products.objects.all():
            self.response_data['data'].append({
            "category":a.category,
            "id":a.id,
            "name":a.name,
            "cant":a.cant,
            "description":a.description,
            "image":a.image,
            #"price":a.price,
            })

    def viveresProductsFilter(self):
        self.response_data['cantTotal']= Products.objects.filter(category=1)
        for a in Products.objects.filter(category=1):
            self.response_data['data'].append({
            "category":a.category,
            "id":a.id,
            "name":a.name,
            "cant":a.cant,
            "description":a.description,
            "image":a.image,
            #"price":a.price,
            })
    def frigorificoProductsFilter(self):
        self.response_data['cantTotal']= Products.objects.filter(category=2)
        for a in Products.objects.filter(category=2):
            self.response_data['data'].append({
            "category":a.category,
            "id":a.id,
            "name":a.name,
            "cant":a.cant,
            "description":a.description,
            "image":a.image,
            #"price":a.price,
            })
    def enlatadosProductsFilter(self):
        self.response_data['cantTotal']= Products.objects.filter(category=3)
        for a in Products.objects.filter(category=3):
            self.response_data['data'].append({
            "category":a.category,
            "id":a.id,
            "name":a.name,
            "cant":a.cant,
            "description":a.description,
            "image":a.image,
            #"price":a.price,
            })
