from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
    display_name = models.CharField(max_length=50)
    home_page = models.URLField(max_length=200, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)
