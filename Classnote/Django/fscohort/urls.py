
from django.urls import path
from .views import students

urlpatterns = [
  
    path('student/',students )
]
