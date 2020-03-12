from pyrebase import pyrebase
from rest_framework import serializers

from employee.models import Employee
from firebase.settings import firebaseConfig


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('name', 'age')

    def create(self, validated_data):
        fire_store_config = pyrebase.initialize_app(firebaseConfig)
        db = fire_store_config.database()
        db.child('employee').push(validated_data)
