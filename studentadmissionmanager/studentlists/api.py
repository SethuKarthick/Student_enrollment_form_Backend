from studentlists.models import StudentInfo
from rest_framework import viewsets, permissions
from .serializers import StudentListSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = StudentInfo.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]
    serializer_class = StudentListSerializer
