from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Department, Personnel
from .serializers import DepartmentSerializer, PersonnelSerializer
from .permissions import IsAdminOrReadOnly


class DepartmentView(ListCreateAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class DepartmentDetail(RetrieveAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class PersonnelView(ListCreateAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


class PersonnelDetail(RetrieveAPIView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]