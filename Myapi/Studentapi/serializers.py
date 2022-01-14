from rest_framework import serializers
from Studentapi.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Student
        fields = ['id','fname','lname','std_id','contact_no']