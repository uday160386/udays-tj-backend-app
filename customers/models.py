# Create your models here.
from django.conf import settings

from rest_framework.authtoken.models import Token as DefaultTokenModel

from .utils import import_callable

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Register your models here.

TokenModel = import_callable(
    getattr(settings, 'REST_AUTH_TOKEN_MODEL', DefaultTokenModel))


class UserManager(BaseUserManager):
    def create_user(self, username, email, gender, first_name, last_name, phone_number, password, confirm_password):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, gender=gender, first_name=first_name, last_name=last_name,
                          phone_number=phone_number,
                          password=password, confirm_password=confirm_password)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, gender, first_name, last_name, phone_number, password,
                         confirm_password):
        user = self.create_user(username=username, email=email, gender=gender, first_name=first_name,
                                last_name=last_name, phone_number=phone_number, password=password,
                                confirm_password=confirm_password)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.activated = True
        user.save(using=self.db)
        return user

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser


class User(PermissionsMixin, AbstractBaseUser):
    add_fieldsets = ('username', 'email', 'gender', 'password', 'confirm_password',
                     'first_name', 'last_name', 'phone_number'),

    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    gender_choices = [("M", "Male"), ("F", "Female"), ("O", "Others")]
    gender = models.CharField(choices=gender_choices, default="M", max_length=1)
    password = models.CharField(max_length=32, blank=True, null=True)
    confirm_password = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    phone_number = models.CharField(max_length=13, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email", "password", "confirm_password", "phone_number", "first_name", "last_name", "gender"]
    USERNAME_FIELD = "username"
    objects = UserManager()

    def get_first_name(self):
        # The user is identified by their email address
        return self.first_name

    def get_last_name(self):
        # The user is identified by their email address
        return self.last_name

    def __str__(self):
        return self.username
