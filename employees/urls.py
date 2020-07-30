from django.urls import path
from . import views

urlpatterns = [
    path('api/employees', views.EmployeeListCreate.as_view() ),
    # path('api/coes', views.CoeListCreate.as_view() ),
]