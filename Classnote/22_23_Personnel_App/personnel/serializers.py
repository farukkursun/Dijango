from rest_framework import serializers

from .models import (
    Department,
    Personnel,
)    

  #fix serializers
class FixSerializer(serializers.ModelSerializer):
    pass

    #serializers


class DepartmentSerializer(FixSerializer):
    class Meta:
        model = Department
        exclude = []


class PersonnelSerializer(FixSerializer):
    class Meta:
        model = Personnel
        exclude = []