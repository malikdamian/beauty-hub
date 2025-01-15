from rest_framework import serializers

from service.models import Category, Service


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("name",)


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ("category", "name", "price", "time", "seat", "note")
