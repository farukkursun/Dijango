from rest_framework import serializers

from .models import (
    Department,
    Personnel,
)    

  #fix serializers
class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()


    #serializers


class DepartmentSerializer(FixSerializer):
    class Meta:
        model = Department
        exclude = []


class PersonnelSerializer(FixSerializer):
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField()
    gender = serializers.CharField(source='get_gender_display')
    title = serializers.CharField(source='get_title_display')
    working_day = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        exclude = []

    def update(self, instance, validated_data):
        if validated_data['is_active'] == False:
            from datetime import datetime
            validated_data['ended'] = datetime.now()
        return super().update(instance, validated_data) 

    def get_working_day(self, object):
        # from datetime import datetime
        # diff = (datetime.now() - object.started.replace(tzinfo=None))
        from django.utils import timezone
        diff = (timezone.now() - object.started)
        return diff.days