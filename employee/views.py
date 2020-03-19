import firebase_admin
from firebase_admin import firestore
from rest_framework.generics import ListCreateAPIView

from employee.serializers import EmployeeSerializer
from firebase.settings import firestore_credentials


class EmployeeList(ListCreateAPIView):

    def get_serializer_class(self):
        return EmployeeSerializer

    def get_queryset(self):
        firebase_admin.initialize_app(firestore_credentials)
        db = firestore.client()
        documents = db.collection('employees').stream()
        for document in documents:
            print("Employees data as following: ", document.to_dict())

    def perform_create(self, serializer):
        firebase_admin.initialize_app(firestore_credentials)
        db = firestore.client()
        employee_data = {'name': 'Akram', 'age': 28}
        db.collection('employees').add(employee_data)
