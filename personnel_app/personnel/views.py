from django.shortcuts import render
from .models import Personnel, Departments 
from .serializers import PersonnelSerializer, DepartmentsSerializer


from rest_framework.viewsets import ModelViewSet

# Create your views here.


class PersonnelMVS(ModelViewSet):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer

class DepartmentsMVS(ModelViewSet):
    queryset = Departments.objects.all()
    serializer_class = DepartmentsSerializer