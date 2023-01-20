from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Department, DepartmentSerializer,
    Personnel, PersonnelSerializer,
)

# ----------------- FixView ------------------

class FixView(ModelViewSet):
    pass

# ----------------- Views ------------------

class DepartmentView(FixView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PersonnelView(FixView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer
