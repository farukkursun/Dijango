

from django.urls import path, include

from django.http import HttpResponse

def home(request):
    return HttpResponse('FsCohort')

urlpatterns = [
    path('', home),
]