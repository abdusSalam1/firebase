from django.urls import path

from employee.views import EmployeeList

urlpatterns = [
    path('employee',EmployeeList.as_view())
]
