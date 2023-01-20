from rest_framework import serializers

from .models import (
    Department,
    Personnel
)

# ----------------- FixSerializer ------------------

class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        validated_data['user_id'] = self.context.get('request').user.id
        return super().create(validated_data)

# ----------------- Serializers ------------------

class DepartmentSerializer(FixSerializer):

    class Meta:
        model = Department
        exclude = []

class PersonnelSerializer(FixSerializer):
    department = serializers.StringRelatedField()
    department_id = serializers.IntegerField()
    gender_info = serializers.CharField(read_only=True, source='get_gender_display') # get choices value.
    title_info = serializers.CharField(read_only=True, source='get_title_display') # get choices value.
    working_day = serializers.SerializerMethodField()

    class Meta:
        model = Personnel
        exclude = []

    def create(self, validated_data):
        from account.models import Account
        from django.contrib.auth.hashers import make_password
        # Rastgele Numara:
        import random
        rnd = str(random.randint(100,999))
        # Personnel oluşturduğunda Account da oluştur:
        Account.objects.create(
            username = validated_data['last_name'] + '_' + rnd,
            # Parolayı şifreleyerek kaydet:
            password = make_password(validated_data['last_name'] + '_' + rnd),
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['first_name'] + '@gmail.com',
            # Giriş yapabilsin:
            is_active = True,
            # Personel Team Lead ise => is_staff = True
            is_staff = True if validated_data['title']==1 else False
        )
        return super().create(validated_data)

    # Çıkış tarihini otomatik yaz:
    def update(self, instance, validated_data):
        if validated_data['is_active'] == False:
            from datetime import datetime
            validated_data['ended'] = datetime.now()
        return super().update(instance, validated_data)

    # Çalışılan gün sayısı hesapla:
    def get_working_day(self, object):
        # from datetime import datetime
        # diff = (datetime.now() - object.started.replace(tzinfo=None))
        from django.utils import timezone
        diff = (timezone.now() - object.started)
        return diff.days