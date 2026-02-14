from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class Users(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)

    joined = models.DateTimeField(auto_now_add=True)
    space_left = models.BigIntegerField(default=5 * 1024 * 1024 * 1024)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
