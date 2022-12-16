from rest_framework import serializers
from .models import Todo


class TodoSerializers(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields= (
            'id',
            'task',
            'description',
            'priority',
            'is_done',
            'created_date'

        )



     