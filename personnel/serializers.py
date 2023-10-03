from rest_framework import serializers

from django.utils.timezone import now

from .models import Department, Personnel


class PersonnelSerializer(serializers.ModelSerializer):

    department = serializers.StringRelatedField() # read only
    department_id = serializers.IntegerField()
    user = serializers.StringRelatedField() #read only
    day_since_jobs = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        fields = (
            'first_name',
            'last_name',
            'title',
            'gender',
            'salary',
            'department',
            'department_id',
            'user',
            'user_id',
            'start_date',
            'id',
            'day_since_jobs',
        )

    def get_day_since_jobs(self, obj):
        return (now() - obj.start_date).days


    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        instance = Personnel.objects.create(**validated_data)
        return instance


class DepartmentSerializer(serializers.ModelSerializer):

    personnel_count = serializers.SerializerMethodField()
    personnels = PersonnelSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = '__all__'
        read_only_fields = ['id','personnels']

    def get_personnel_count(self, obj):
        return obj.personnels.count()
