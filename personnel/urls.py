from django.urls import path, include

from .views import DepartmentView, PersonnelView, PersonnelDetail, DepartmentDetail

urlpatterns = [
    path('departments/', DepartmentView.as_view()),
    path('personnels/', PersonnelView.as_view()),
    path('departments/<int:pk>/', DepartmentDetail.as_view()),
    path('personnels/<int:pk>/', PersonnelDetail.as_view()),
]