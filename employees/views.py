from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin
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

class EmployeesView(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        # retrieve all employee objects from DB
        queryset = Employee.objects.all()

        # get coe_id and coe query params. If any one of them is present, filter
        # the request would look like:
        #       http://127.0.0.1:8000/api/employees?coe_id=AFTC0628
        #       http://127.0.0.1:8000/api/employees?coe=COE%20TEst
        queryParamCoeId = self.request.query_params.get('coe_id', None)
        # queryParamCoe = self.request.query_params.get('coe', None)   

        if queryParamCoeId is not None:
           queryset = queryset.filter(coe_id=queryParamCoeId)
            
        return queryset

class EmployeeView(GenericAPIView, UpdateModelMixin):
    def get(self, request, *args, **kwargs):
        # retrieve the empId variable from the URL
        if (kwargs.get('empId') is not None):
            empId = kwargs['empId']
        else:
            return HttpResponse('Invalid request - empId not found', statu = 400)
        
        # get data for employee with id = empId 
        self.queryset = Employee.objects.get(id = empId)
        self.kwargs['pk'] = empId
        
        # get data for employee with id = empId 
        employee = Employee.objects.get(id = empId)

        # serialize the data
        data = EmployeeSerializer(employee).data

        #return the data as Json
        return JsonResponse(data, safe=False)

    def put(self, request, *args, **kwargs):
        # retrieve the empId variable from the URL
        if (kwargs.get('empId') is not None):
            empId = kwargs['empId']
        else:
            return HttpResponse('Invalid request - empId not found', statu = 400)
        
        # get data for employee with id = empId 
        self.queryset = Employee.objects.get(id = empId)
        self.kwargs['pk'] = empId
        
        return self.partial_update(request, *args, **kwargs)

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
