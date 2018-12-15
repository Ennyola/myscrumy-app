from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	"""docstring for UserSerializier"""
	class Meta:
		model = User
		fields = ['username']


class ScrumGoalsSerializer(serializers.ModelSerializer):
	"""docstring for UserSerializier"""
	class Meta:
		model = ScrumGoal
		fields = ('id','name','status')


class ScrumUserSerializer(serializers.ModelSerializer):
	"""docstring for UserSerializier"""
	scrumgoal_set = ScrumGoalsSerializer(many = True)
	class Meta:
		model = ScrumUser
		fields = ('nickname', 'scrumgoal_set')


