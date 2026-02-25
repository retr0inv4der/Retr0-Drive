from django.contrib.auth.base_user import BaseUserManager
from django.db.models import Manager
from django.db import models

class MyUserManager(BaseUserManager) : 
    
    def create_user(self ,username ,  email , password , **extra_fields): 
        if not email :
            raise ValueError("email is required")
        if not username :
            raise ValueError("username is required")
        if not password : 
            raise ValueError("password is required ")

        email = self.normalize_email(email) 
        user = self.model(username = username , email = email , **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self ,username , email , password , **extra_fields) : 
        extra_fields.setdefault("is_staff" , True ) 
        extra_fields.setdefault("is_superuser" , True)
        return self.create_user(username , email , password , **extra_fields)
       
