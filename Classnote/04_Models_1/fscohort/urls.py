from django.urls import path, include
from .views import fscohort, fscohort2
# must be in views.py:
urlpatterns = [
    path('', fscohort),
    path('example/', fscohort2),
]