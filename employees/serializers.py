from rest_framework import serializers
from .models import Employee, Quarterly

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'first_name', 'last_name', 'manager_id', 'manager_name', 'du_head_id', 'du_head_name', 'date_of_joining', 'email', 'designation', 'service_status', 'project_id', 'project_name', 'project_start_date', 'project_end_date', 'coe_id', 'coe')

class CoeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee