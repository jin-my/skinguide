from django.db import models
from django.contrib.auth.models import AbstractUser
from skinguide import settings
from django import forms
#from django.contrib.auth.models import User
# Create your models here.
class User(AbstractUser):
    # id password last_login is_superuser username first_name last_name email is_staff is_activate date_joinedㄴ
    #username = models.CharField(max_length = 10)
    skintype=models.CharField(max_length=5, null = True)
    gender=models.CharField(max_length=2, null = True)

