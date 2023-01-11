from rest_framework import serializers
from django.contrib.auth.models import User



class RegisterSerializers(serializers.ModelSerializer):
  


    class Meta:
        model = User
        exclude = [
        "last_login",
        "date_joined",
        "groups",
        "user_permissions",
    ]


     # Override: Attributeleri doğrularken parolayı valid+hash yap:
    def validate(self, attrs):
        from django.contrib.auth.hashers import make_password # şifreleme fonksiyonu
        from django.contrib.auth.password_validation import validate_password # doğrulama fonksiyonu
        password = attrs.get('password') # attrs'dan parolayı al.
        validate_password(password) # validators kontrölünden geçir. (yoksa hata ver)
        attrs.update({'password': make_password(password)}) # parolayı şifrele.
        return super().validate(attrs) # orjinal methodu çalıştır.