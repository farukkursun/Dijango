from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    # email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Account
        exclude = [
            'date_joined',
            'groups',
            'user_permissions',
        ]

    # Override:
    def create(self, validated_data):
        validated_data['is_active'] = True
        return super().create(validated_data)

    # Override:
    def validate(self, attrs):
        from django.contrib.auth.hashers import make_password
        from django.contrib.auth.password_validation import validate_password
        password = attrs.get('password')
        validate_password(password) # Validation
        encrypt_password = make_password(password) # Encrypt
        attrs.update({'password': encrypt_password})
        return attrs

# TOKEN
from dj_rest_auth.serializers import TokenSerializer

class TokenUserSerializer(TokenSerializer):

    user = AccountSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = ('key', 'user')