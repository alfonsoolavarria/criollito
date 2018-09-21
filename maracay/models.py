from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Products(models.Model):
    __cate=((1,_('Viveres')),(2,_('Frigorifico')),(3,_('Enlatados')))
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    price=models.DecimalField(max_digits=30, decimal_places=2)
    description=models.CharField(max_length=100)
    image=models.CharField(max_length=50)
    cant=models.PositiveSmallIntegerField(default=1)
    category=models.PositiveSmallIntegerField(choices=__cate)
    create_at=models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.OneToOneField(User, related_name='user_profile',on_delete=models.CASCADE)
    phone=models.CharField(max_length=50)
    direction=models.CharField(max_length=100)
    tw=models.CharField(max_length=50)
    fb=models.CharField(max_length=50)
    google=models.CharField(max_length=50)

class Tools(models.Model):
    id=models.AutoField(primary_key=True)
    costoenvio=models.PositiveSmallIntegerField(default=10)
    create_at=models.DateTimeField(auto_now_add=True)
