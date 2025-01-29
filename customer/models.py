from django.db import models

from service.models import TimeStampMixin


class Customer(TimeStampMixin):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(null=True)
    note = models.CharField(max_length=512, null=True)
