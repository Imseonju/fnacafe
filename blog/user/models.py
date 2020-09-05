from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    name = models.CharField(max_length= 10, null = True, blank = True)
    phone = models.CharField(max_length= 12, null = True, blank = True)
    age = models.CharField(max_length= 2, null = True, blank = True)
