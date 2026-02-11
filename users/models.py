from django.db import models
from django.db.models.functions import Now
# Create your models here.

class Users(models.Model) : 
    username = models.CharField(max_length=20) 
    password = models.CharField(max_length=50)
    joined = models.DateTimeField(auto_now_add=True)
    space_left = models.DecimalField(max_digits=20 , default=5368709120)
