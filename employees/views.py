from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics

# Create your views here.
class EmployeeListCreate(generics.ListCreateAPIView):
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

# class CoeListCreate(generics.ListCreateAPIView):

#     class CoeClass:
#         def __init__(self, coeId=None, coeName=None):
#             self.coeName = coeName
#             self.coeId = coeId

#     coeDictionary = dict()

#     allEmployees = Employee.objects.all()

#     for employee in allEmployees:
#         coeDictionary[employee.coe_id] = CoeClass(employee.coe_id, employee.coe)
    

