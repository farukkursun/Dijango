from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return HttpResponse('Hello this is our hpme page ...')

def students(request):

    return HttpResponse('ali, veli, deli')

