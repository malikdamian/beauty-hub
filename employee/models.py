from django.contrib.auth.models import AbstractUser
from django.db import models


class Employee(AbstractUser):
    phone = models.CharField(max_length=15, null=True)
    specialization = models.CharField(max_length=128, null=True)
    photo = models.BinaryField(null=True)
    modified_at = models.DateTimeField(auto_now=True)
