from django.db import models

from chef.models import Chef
# Create your models here.
# 530016

class Food(models.Model):
	TYPE_OF_DIET_CHOICES = (
		("VG","Vegetarian"),
		("NVG","Non-vegetarian"),
		)
	MEAL_CHOICES = (
		("LNCH","Lunch"),
		("DNR","Dinner"),
		)
	TIME_SLOT_CHOICES = (
		("12 p.m. to 1 p.m.","12 p.m. to 1 p.m."),
		("1 p.m. to 2 p.m.","1 p.m. to 2 p.m."),
		("2 p.m. to 3 p.m.","2 p.m. to 3 p.m."),
		("3 p.m. to 4 p.m.","3 p.m. to 4 p.m."),
		("4 p.m. to 5 p.m.","4 p.m. to 5 p.m."),
		("7 p.m. to 8 p.m.","7 p.m. to 8 p.m."),
		("8 p.m. to 9 p.m.","8 p.m. to 9 p.m."),
		("9 p.m. to 10 p.m.","9 p.m. to 10 p.m."),
		("10 p.m. to 11 p.m.","10 p.m. to 11 p.m."),
		)


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




	name = models.CharField(max_length=255)
	description = models.TextField()
	type_of_diet = models.CharField(max_length=3,choices=TYPE_OF_DIET_CHOICES)
	
	picture = models.ImageField(upload_to="food_images/%Y/%m/%d")

	meal_timing = models.CharField(max_length=4,choices = MEAL_CHOICES)
	time_slot = models.CharField(max_length=30,choices=TIME_SLOT_CHOICES)
	day = models.DateField()

	served_by = models.ForeignKey(Chef)
	location = models.CharField(max_length=6,choices =PINCODES)

	price = models.IntegerField()

	quantity = models.IntegerField(default=0)

	hash_tags = models.CharField(max_length=255,null=True,blank=True)

	def __unicode__(self):
		return self.name

	def decrement_quantity(self,no_of_quantities):
		if self.quantity >= no_of_quantities:
			self.quantity -= no_of_quantities
			self.save()
			return True
		else:
			return False



class Coupon(models.Model):
	coupon_code = models.CharField(max_length=10);
	discount = models.IntegerField()
	max_discount = models.IntegerField()
	minimum_order = models.IntegerField()