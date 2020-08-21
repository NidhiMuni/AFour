from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
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

class EmployeeView(
        RetrieveModelMixin,
        GenericAPIView, 
        UpdateModelMixin):
    serializer_class = EmployeeSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        # Check if manager_id was changed
        newManagerId = self.request.data.get('manager_id')

        if newManagerId is not None:
            # This means that manager_id is being updated
            # Fetch the data for newManagerId from employee table
            try:
                # Now, fetch the data for the new manager
                newManagerData = Employee.objects.get(id = newManagerId)
            except:
                return HttpResponseBadRequest('New manager_id is invalid')

            # update the employee row with new manager id and name
            self.request.data['manager_name'] = newManagerData.first_name + ' ' + newManagerData.last_name

        return self.partial_update(request, *args, **kwargs)

    # Request PUT /api/employees/AFTD002 with payload {"coe_id": "BFTD0648", "coe": "COE Test Hello", "email": "test@test2.com"}
    def get_queryset(self):
        # user filter and not get because filter returns a queryset and not get
        empId = self.kwargs['id']
        return Employee.objects.filter(id = empId)

class QuarterlyReviewView(generics.ListCreateAPIView):
    serializer_class = QuarterlyReviewSerializer

    def get_queryset(self):
        # retrieve all employee objects from DB
        queryset = QuarterlyReview.objects.all()

        queryParamEmployeeId = self.request.query_params.get('employee_id', None)
        # queryParamCoe = self.request.query_params.get('coe', None)   

        if queryParamEmployeeId is not None:
           queryset = queryset.filter(employee_id=queryParamEmployeeId)
            
        return queryset
