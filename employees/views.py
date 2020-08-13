from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Employee, QuarterlyReview
from .serializers import EmployeeSerializer, QuarterlyReviewSerializer
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

import json

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

#serializers.register_serializer('json', 'employees.serializers.EmployeeSerializer')

class EmployeeListCreate(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    logger.warning(EmployeeSerializer)

    def get_queryset(self):
        # retrieve all employee objects from DB
        queryset = Employee.objects.all()

        logger.warning('In EmployeeListCreate view!!')
        # get coe_id and coe query params. If any one of them is present, filter
        # the request would look like:
        #       http://127.0.0.1:8000/api/employees?coe_id=AFTC0628
        #       http://127.0.0.1:8000/api/employees?coe=COE%20TEst
        queryParamCoeId = self.request.query_params.get('coe_id', None)
        # queryParamCoe = self.request.query_params.get('coe', None)   

        if queryParamCoeId is not None:
           queryset = queryset.filter(coe_id=queryParamCoeId)
            
        return queryset

class EmployeeView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer


    @csrf_exempt #make the request exempt from providing CSRF cookie
    def emp_by_id(request, empId):


        if request.method == 'GET':
            # get data for employee with id = empId 
            employee = Employee.objects.get(id = empId)

            # serialize the data
            data = EmployeeSerializer(employee).data

            #return the data as Json
            return JsonResponse(data, safe=False)

        elif request.method == 'PUT':
            receivedPayload = json.loads(request.body.decode('utf-8'))
            employee = Employee.objects.get(id = empId)
            employee.update_fields(receivedPayload)
            employee.save()
            return HttpResponse(status=201)
          
        
class QuarterlyReviewListCreate(generics.ListCreateAPIView):
    serializer_class = QuarterlyReviewSerializer

    def get_queryset(self):
        # retrieve all employee objects from DB
        queryset = QuarterlyReview.objects.all()

        # get coe_id and coe query params. If any one of them is present, filter
        # the request would look like:
        #       http://127.0.0.1:8000/api/employees?coe_id=AFTC0628
        #       http://127.0.0.1:8000/api/employees?coe=COE%20TEst
        queryParamEmployeeId = self.request.query_params.get('employee_id', None)
        # queryParamCoe = self.request.query_params.get('coe', None)   

        if queryParamEmployeeId is not None:
           queryset = queryset.filter(employee_id=queryParamEmployeeId)
            
        return queryset
