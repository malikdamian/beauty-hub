from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self) -> str:
        return f"Category: {self.name}"


class Service(models.Model):
    category = models.OneToOneField(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    time = models.FloatField()
    seat = models.CharField(max_length=128, null=True)
    note = models.CharField(max_length=2048, null=True)

    def __str__(self) -> str:
        return f"Service: {self.name}"
