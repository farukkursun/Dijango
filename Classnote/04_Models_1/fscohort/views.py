from django.shortcuts import render
from django.http import HttpResponse




def fscohort(request):
    return HttpResponse('''
    <p><b>
        Welcome to FsCohort
    </b></p>
''')

def fscohort2(request):
    return HttpResponse('''
    <p><b>
        Welcome to SubFolder
    </b></p>
''')


