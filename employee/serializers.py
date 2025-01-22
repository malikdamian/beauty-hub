from rest_framework import serializers

from employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = (
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "specialization",
            "modified_at",
        )
