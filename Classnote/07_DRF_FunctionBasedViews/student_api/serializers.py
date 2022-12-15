from rest_framework import serializers
from .models import Student, Path

# class StudentSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=30)
#     last_name = serializers.CharField(max_length=30)
#     number = serializers.IntegerField(required=False)
    
#     def create(self, validated_data):
#         return Student.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.first_name = validated_data.get('first_name', instance.first_name)
#         instance.last_name = validated_data.get('last_name', instance.last_name)
#         instance.number = validated_data.get('number', instance.number)
#         instance.save()
#         return instance



class StudentSerializer(serializers.ModelSerializer):
    full_name= serializers.SerializerMethodField()
    path= serializers.StringRelatedField()
    path_id= serializers.IntegerField()
    class Meta:
        model = Student
        # fields= '__all__'
        fields = [
            "id", 
        'path', 
        "first_name",
         "last_name", 
         "number", 
         "full_name",
          'path_id']

    def get_full_name(self, obj):
        return f'{obj.first_name} - {obj.last_name}'


class PathSerializer(serializers.ModelSerializer):
    # students = StudentSerializer(many=True)
    
    students = serializers.HyperlinkedRelatedField(
        many= True,
        read_only = True,
        view_name = "detail"
    )
    
    class Meta:
        model = Path
        fields = ["id", "path_name", "students" ]