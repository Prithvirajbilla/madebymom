from django.db import models
import re
import uuid
from django.core import validators
from django.utils import timezone
from django.utils.http import urlquote
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django import forms
 
 
class Order(models.Model):
	PINCODES = (
		('530003', 'Andhra University'),
		('530003', 'Chinawaltair'),
		('530004', 'Waltair'),
		('530016', 'Akkayapalem'),
		('530016', 'Dwarakanagar'),
		('530017', 'Isakathota'),
		('530017', 'L B Colony'),
		('530017', 'M.V.P COLONY'),
		('530020', 'Dabagardens'),
		('530022', 'H B Colony'),
		('530041', 'Pothinamallayapalem'),
		('530045', 'Gitam Engg. College'),
		('530045', 'Sagar Nagar'),
		('530045', 'Yandada'),
		('530048', 'Madhurawada'),
		('531032', 'Venkupalem'))
	name = models.CharField(max_length=20)
	email = models.EmailField()
	mobile = models.CharField(max_length=10)
	address_line_1 = models.TextField()
	address_line_2 = models.TextField()
	area = models.CharField(max_length=6,choices =PINCODES)

	def __unicode__(self):
		return self.name+" "+self.area

