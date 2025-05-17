from rest_framework import serializers
from staff.models import Employee, Role
from api.user.serializers import UserSerializer




class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    role = serializers.PrimaryKeyRelatedField(queryset=Role.objects.all())

    class Meta:
        model = Employee
        fields = ['id', 'user', 'role', 'email', 'salary', 'hire_date', 'experience_years']
        read_only_fields = ['hire_date']


