from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseBadRequest
from rest_framework.parsers import JSONParser
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from .models import Employee, QuarterlyReview, YearlyReview
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
        empId = self.kwargs['id']

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

            # fetch the employee records from Quarterly table
            quarterlyReviews = QuarterlyReview.objects.filter(employee_id = empId, workflow_status = -100)

            # update the row(s) with new manager's data. Note: there can be multiple records for the same employee                                           v v v vg 
            for qr in quarterlyReviews:
                qr.manager_id = newManagerData.id
                qr.manager_name = newManagerData.first_name + ' ' + newManagerData.last_name
                qr.manager_email = newManagerData.email
                qr.save()

            # fetch the employee records from Yearly table   
            yearlyReviews = YearlyReview.objects.filter(employee_id = empId, workflow_status = -100)

            # update the row(s) with new manager's data. Note: there can be multiple records for the same employee                                           v v v vg 
            for yr in yearlyReviews:
                yr.manager_id = newManagerData.id
                yr.manager_name = newManagerData.first_name + ' ' + newManagerData.last_name
                yr.manager_email = newManagerData.email
                yr.save()

        # Check if du_head was changed
        newDUHeadId = self.request.data.get('du_head_id')

        if newDUHeadId is not None:
            # This means that duhead_id is being updated
            # Fetch the data for newDUheadID from employee table
            try:
                # Now, fetch the data for the new manager
                newDUHeadData = Employee.objects.get(id = newDUHeadId)
            except:
                return HttpResponseBadRequest('New du_head_id is invalid')
   
            # update the employee row with new manager id and name
            self.request.data['du_head_name'] = newDUHeadData.first_name + ' ' + newDUHeadData.last_name

            # fetch the employee records from Quarterly table
            quarterlyReviews = QuarterlyReview.objects.filter(employee_id = empId, workflow_status = -100)

            # update the row(s) with new du head's data. Note: there can be multiple records for the same employee                                           v v v vg 
            for qr in quarterlyReviews:
                qr.du_head_id = newDUHeadData.id
                qr.du_head_name = newDUHeadData.first_name + ' ' + newDUHeadData.last_name
                qr.du_head_email = newDUHeadData.email
                qr.save()

            # fetch the employee records from Yearly table   
            yearlyReviews = YearlyReview.objects.filter(employee_id = empId, workflow_status = -100)

            # update the row(s) with new du head's data. Note: there can be multiple records for the same employee                                           v v v vg 
            for yr in yearlyReviews:
                yr.du_head_id = newDUHeadData.id
                yr.du_head_name = newDUHeadData.first_name + ' ' + newDUHeadData.last_name
                yr.du_head_email = newDUHeadData.email
                yr.save()

        # Check if coe id was changed
        newCOEId = self.request.data.get('coe_id')

        if newCOEId is not None:
            # This means that coe id is being updated
            try:
                # Now, fetch the data for the new coe
                newCOEData = Employee.objects.get(id = newCOEId)
            except:
                return HttpResponseBadRequest('New coe_id is invalid')
   
            # update the employee row with new coe id and name
            self.request.data['coe'] = newCOEData.first_name + ' ' + newCOEData.last_name

            # fetch the employee records from Quarterly table
            quarterlyReviews = QuarterlyReview.objects.filter(employee_id = empId, workflow_status = -100)

            # update the row(s) with new coe head's data. Note: there can be multiple records for the same employee                                           v v v vg 
            for qr in quarterlyReviews:
                qr.coe_head_id = newCOEData.id
                qr.coe_head_name = newCOEData.first_name + ' ' + newCOEData.last_name
                qr.save()

            # fetch the employee records from Yearly table   
            yearlyReviews = YearlyReview.objects.filter(employee_id = empId, workflow_status = -100)

            # update the row(s) with new coe head's data. Note: there can be multiple records for the same employee                                           v v v vg 
            for yr in yearlyReviews:
                yr.coe_head_id = newCOEData.id
                yr.coe_head_name = newCOEData.first_name + ' ' + newCOEData.last_name
                yr.save()
                

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
