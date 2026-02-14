from django.db import models
from django.db.models.functions import Now
# Create your models here.

class Users(models.Model) : 
    username = models.CharField(max_length=20 , unique=True) 
    password = models.CharField(max_length=50)
    joined = models.DateTimeField(auto_now_add=True)
    space_left = models.DecimalField (decimal_places=20 , max_digits=20 , default=5368709120)
