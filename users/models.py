from django.db import models
import re
import uuid
from django.core import validators
from django.utils import timezone
from django.utils.http import urlquote
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django import forms
from food.models import Food
 
class Order(models.Model):
	PINCODES = ('Andhra University','Chinawaltair','Waltair','Akkayapalem','Dwarakanagar',
		'Isakathota','L B Colony','M.V.P COLONY','Dabagardens','H B Colony',
		'Pothinamallayapalem','Gitam Engg. College','Sagar Nagar','Yandada',
		'Madhurawada','Venkupalem')

	name = models.CharField(max_length=20)
	email = models.EmailField()
	mobile = models.CharField(max_length=10)
	address_line_1 = models.TextField()
	address_line_2 = models.TextField()
	area = models.CharField(max_length=30)

	def __unicode__(self):
		return self.name+" "+self.area


class Cart(models.Model):
	order = models.ForeignKey(Order)
	discount = models.IntegerField();

	def __unicode__(self):
		return str(self.pk)


class Item(models.Model):
	cart = models.ForeignKey(Cart)
	food = models.ForeignKey(Food)
	quantity = models.IntegerField()

	def __unicode__(self):
		return str(self.pk)
