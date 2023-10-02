from rest_framework import serializers

from .models import Personnel, Departments


class PersonnelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Personnel
        fields = (
            'first_name',
            'last_name',
            'title',
            'gender',
            'salary',
            'department',
            'user',
        )


class DepartmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Departments
        fields = (
            'name',
        )

    def create(self, validated_data):
        return Departments.objects.all()