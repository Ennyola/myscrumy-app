from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ScrumUser(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	nickname = models.CharField(max_length = 50)
	age = models.IntegerField(default = 0) 
	
	def __str__(self):
		return self.nickname
		
class ScrumGoal(models.Model):
	user = models.ForeignKey(ScrumUser, on_delete=models.CASCADE)
	name = models.CharField(max_length = 140)

	'''
	0 = weekly Goal
	1 = Daily Target 
	2 = Verify
	3 = Done
	'''

	status = models.IntegerField(default = 1)

	def __str__():
		return self.name