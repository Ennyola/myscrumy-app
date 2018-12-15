from django.contrib import admin
from .models import ScrumUser,ScrumGoal

# Register your models here.
admin.site.register(ScrumUser)
admin.site.register(ScrumGoal)