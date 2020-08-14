from django.urls import path
from . import views

urlpatterns = [
    path('api/employees', views.EmployeesView.as_view() ),
    path('api/employees/<slug:id>', views.EmployeeView.as_view() ), # allows any slug string (https://docs.djangoproject.com/en/3.1/topics/http/urls/)
    path('api/quarterlyreview', views.QuarterlyReviewView.as_view() ),
]