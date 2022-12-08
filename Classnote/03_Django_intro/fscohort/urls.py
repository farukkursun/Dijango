
from django.urls import path
from .views import students,home

urlpatterns = [
    path('home/', home),
    path('student/',students )
]
