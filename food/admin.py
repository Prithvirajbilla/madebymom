from django.contrib import admin
from django import forms
from django.db import models
from food.models import Food,Coupon
from users.models import *

class FoodAdmin(admin.ModelAdmin):
    formfield_overrides = { models.TextField: {'widget': forms.Textarea(attrs={'class':'ckeditor'})}, }

    class Media:
        js = ('ckeditor/ckeditor.js',)

admin.site.register(Food,FoodAdmin)

admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Item)