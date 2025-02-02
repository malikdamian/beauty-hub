from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "note",
            "created_at",
            "modified_at",
        )
