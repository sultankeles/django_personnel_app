from django.urls import path, include

from .views import PersonnelMVS, DepartmentsMVS

from rest_framework import routers


router = routers.DefaultRouter()
router.register('personnel_mvs', PersonnelMVS)
router.register('departments_mvs', DepartmentsMVS)

urlpatterns = [
     path("", include(router.urls)),
]
