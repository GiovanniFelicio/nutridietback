from django.db import models
from django.contrib.auth.models import AbstractUser

from core.manager.user_manager import UserManager


class User(AbstractUser):
    REQUIRED_FIELDS = ['email', 'password']

    email = models.EmailField(name='email', unique=True)
    username = models.CharField(name='username', max_length=30, null=False, unique=True)
    password = models.CharField(name='password', max_length=255, null=False)
    date_birth = models.DateField(name='date_birth', null=True)
    is_active = models.BooleanField(name='active', default=True)
    is_admin = models.BooleanField(name='is_admin', default=False)
    is_staff = models.BooleanField(name='is_staff', default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    created_at = models.DateTimeField(name='created_at', auto_now_add=True)
    updated_at = models.DateTimeField(name='updated_at', auto_now_add=True)

    objects = UserManager()

    @property
    def is_superuser(self):
        return self.is_admin

    class Meta:
        db_table = 'user'

    def __str__(self):
        return self.first_name + ' ' + self.last_name
