from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import MyUserManager

class Users(AbstractBaseUser , PermissionsMixin) : 
    username = models.CharField(max_length=20, unique=True)
    email = models.EmailField(unique=True)
    space_left = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username" 
    REQUIRED_FIELDS = ["email"]
    objects = MyUserManager()
    
    

