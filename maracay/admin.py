from django.contrib import admin
from .models import Tools, Profile as ProfileDB, PurchaseConfirmation, TokenPassword, Product, Shopping, purchaseHistory
# Register your models here.

admin.site.register(Product)
admin.site.register(Tools)
admin.site.register(Shopping)
admin.site.register(PurchaseConfirmation)
admin.site.register(purchaseHistory)
