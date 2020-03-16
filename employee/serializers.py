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
        auth = fire_store_config.auth()
        user = auth.sign_in_with_email_and_password("abdus.salam111@yahoo.com", "5qVpDGQy4tSEcR5")
        db = fire_store_config.database()
        print("Got to the saving ")
        db.child('employee').push({"name":"akram", "age":27}, user['idToken'])
        print("Saved Data")
