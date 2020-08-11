from django.shortcuts import render
from .models import Employee, QuarterlyReview
from .serializers import EmployeeSerializer, QuarterlyReviewSerializer
from rest_framework import generics

# import the logging library
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

class EmployeeListCreate(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer
    
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

class Employees(generics.ListCreateAPIView):
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        # retrieve all employee objects from DB
        queryset = Employee.objects.all()

        logger.warning('Retrieved employees. Count = %s', queryset.count())
           
        empId = self.request.GET.get('empId', None)

        logger.warning('Path = %s', empId)

        return queryset
  



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
