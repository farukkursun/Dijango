from django.contrib.auth.models import User
from .serializers import RegisterSerializers
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


class RegisterView(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [IsAdminUser]