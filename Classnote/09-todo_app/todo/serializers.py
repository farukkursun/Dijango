from rest_framework import serializers
from .models import Todo


class TodoSerializers(serializers.ModelSerializer):
    todo_detail = serializers.HyperlinkedIdentityField(
        view_name='todo-detail',
    )

    class Meta:
        model = Todo
        fields = (
            'id',
            'todo_detail',
            'task',
            'description',
            'priority',
            'is_done',
            'created_date'
        )


     