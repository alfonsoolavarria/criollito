from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from .views import Maracay, Account, Conditions,Login,Logout,Profile, Help, We, Places, Payment, Delivery
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    url(r'^$', Maracay.as_view(), name='maracay'),
    url(r'account/$', Account.as_view(), name='account'),
    url(r'conditions/$', Conditions, name='Conditions'),
    url(r'^login/$', csrf_exempt(Login.as_view()), name='login'),
    url(r'^logout/$', csrf_exempt(Logout.as_view()), name='logout'),
    url(r'^profile/$', csrf_exempt(Profile.as_view()), name='profile'),
    url(r'^help/$', Help, name='help'),
    url(r'^we/$', We, name='we'),
    url(r'^places/$', Places, name='places'),
    url(r'^payment/$', Payment, name='payment'),
    url(r'^delivery/$', Delivery, name='delivery'),
]
