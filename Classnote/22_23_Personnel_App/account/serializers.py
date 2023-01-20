from rest_framework import serializers
from .models import Account


class AccountSerializers(serializers.ModelSerializer):
  
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField( required=True)
    # email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

   

    class Meta:
        model = Account
        exclude =[
           "date_joined",
            "groups",
            "user_permissions",

            ]


    def create(self, validated_data):
        validated_data['is_active']=True
        return super().create(validated_data)        


    def validate(self, attrs):
        from django.contrib.auth.hashers import make_password
        from django.contrib.auth.password_validation import validate_password
        password = attrs.get('password')
        validate_password(password)
        encrypt_password = make_password(password)
        attrs.update({'password': encrypt_password})
        return attrs



          