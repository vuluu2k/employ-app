from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Departments, Employees
from EmployeeApp.serializers import DepartmentSerializers, EmployeeAppSerializers


# Create your views here.

@csrf_exempt
def DepartmentApi(request, id=0):
    if request.method == 'GET':
        departments = Departments.objects.all()
        department_serializer = DepartmentSerializers(departments, many=True)
        return JsonResponse(department_serializer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializers(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Add successfully", safe=False)
        return JsonResponse("Add Fail", safe=False)
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        department_serializer = DepartmentSerializers(
            department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Put successfully", safe=False)
        return JsonResponse("Put Fail", safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(
            DepartmentId=department_data['DepartmentId'])
        department.delete()
        return JsonResponse("Delete successfully", safe=False)
