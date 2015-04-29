from django.db import models

# Create your models here.

class Chef(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	picture = models.ImageField(upload_to="pic_folder/")
	rated_users = models.IntegerField()
	accumalted_rating = models.IntegerField()
	served_dishes = models.IntegerField()

	def __unicode__(self):
		return self.name

	def get_rating(self):
		return (self.accumalted_rating*1./self.rated_users)

	def rate_chef(self,rating):
		self.accumalted_rating+=rating
		self.rated_users+=1
		self.save()
		return True

	def add_served_dishes(self,no_of_dishes):
		self.served_dishes+=no_of_dishes
		self.save()
		return True
