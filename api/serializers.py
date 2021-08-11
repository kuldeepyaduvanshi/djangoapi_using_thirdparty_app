from rest_framework import serializers
from api.models import Employee

class EmployeeSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=50)
	role = serializers.CharField(max_length=20)
	address = serializers.CharField(max_length=20)
	salary = serializers.CharField(max_length=10)


