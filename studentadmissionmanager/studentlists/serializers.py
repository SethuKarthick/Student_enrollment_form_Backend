from rest_framework import serializers
from studentlists.models import StudentInfo


class StudentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = '__all__'
