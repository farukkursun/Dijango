from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Account, AccountSerializer
)

class AccountView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
