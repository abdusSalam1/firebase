from rest_framework.generics import ListCreateAPIView

from employee.serializers import EmployeeSerializer


class EmployeeList(ListCreateAPIView):

    def get_serializer_class(self):
        return EmployeeSerializer
