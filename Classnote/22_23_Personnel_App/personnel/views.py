from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import (Department, Personnel)
from .serializers import (DepartmentSerializer, PersonnelSerializer)


   #fix view
class FixView(ModelViewSet):
    pass


   #fix view

class DepartmentView(FixView):
    queryset =Department.objects.all()
    serializer_class = DepartmentSerializer

class PersonnelView(FixView):
    queryset = Personnel.objects.all()
    serializer_class = PersonnelSerializer    
