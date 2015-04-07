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
		)


	name = models.CharField(max_length=255)
	description = models.TextField()
	type_of_diet = models.CharField(max_length=3,choices=TYPE_OF_DIET_CHOICES)
	
	picture = models.ImageField(upload_to="food_images")

	meal_timing = models.CharField(max_length=4,choices = MEAL_CHOICES)
	time_slot = models.CharField(max_length=30,choices=TIME_SLOT_CHOICES)
	day = models.DateField()

	served_by = models.ForeignKey(Chef)
	location = models.CharField(max_length=6,choices =PINCODES)

	price = models.IntegerField()

	quantity = models.IntegerField(default=0)


	def __unicode__(self):
		return self.name

	def decrement_quantity(self,no_of_quantities):
		if self.quantity >= no_of_quantities:
			self.quantity -= no_of_quantities
			self.save()
			return True
		else:
			return False