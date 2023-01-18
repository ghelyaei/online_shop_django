from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser
from .managers import UserManager

class User(AbstractBaseUser):
    email = models.EmailField(max_length=225, unique=True)
    phone_number = models.CharField(max_length=11, unique=True)
    full_name = models.CharField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)


    object = UserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perm(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

