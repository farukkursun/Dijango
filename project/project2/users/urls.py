from django.urls import path, include
from rest_framework import routers
from .views import RegisterView


router = routers.DefaultRouter()
router.register('register', RegisterView)

urlpatterns = [
    
    path('auth/', include('dj_rest_auth.urls')),
    path('', include(router.urls)),
]