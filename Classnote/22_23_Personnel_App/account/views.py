

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .serializers import(
    Account, AccountSerializers
)


class AccountView(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializers