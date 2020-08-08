from django.urls import path
from . import views

urlpatterns = [
    path('api/employees', views.EmployeeListCreate.as_view() ),
    path('api/quarterlyreview', views.QuarterlyReviewListCreate.as_view() ),
]