from django.shortcuts import render,HttpResponse
import io 
from rest_framework.parsers import JSONParser
from api.models import Employee
from api.serializers import EmployeeSerializer
from rest_framework.renderers import JSONRenderer
import requests
import json

# Create your views here.
   
def index(request):
	return HttpResponse("this is allright")

def employeeapi(request):
	if request.method == 'GET':
		json_data = request.body
		stream = io.BytesIO(json_data)
		pythondata = JSONParser().parse(stream)
		id = pythondata.get('id',None)
		if id is not None:
			emp = Employee.objects.get(id=id)
			serializer = EmployeeSerializer(emp)
			json_data = JSONRenderer().render(serializer.data)
			return HttpResponse(json_data,content_type='application/json')
		emp = Employee.objects.all()
		serializer = EmployeeSerializer(emp,many=True)
		json_data = JSONRenderer().render(serializer.data)
		return HttpResponse(json_data,content_type='application/json')
		return render(request,"index.html" , {'json_data' : json_data})

