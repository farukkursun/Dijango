
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import logout

urlpatterns = [
   
    path('login/', obtain_auth_token),
    path('logout/',logout)
]



