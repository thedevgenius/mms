from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):    
        user = self.model(username = username, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user
    

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, password, **extra_fields)


class User(AbstractUser):

    objects = UserManager()

    def __str__(self):
        return f"{self.first_name}"