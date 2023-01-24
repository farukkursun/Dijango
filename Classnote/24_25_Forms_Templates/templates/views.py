from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def hello(request):
    context = {
        'title': 'clarusway is BEST bootcamp'.lower(),
        'dict1': {'django': 'best framework'},
        'my_list': [2, 3, 4],
        'is_exist': True
    }
    return render(request, 'hello.html', context)

'''
    DTL:
        {% DTL Commands %}
        {{ DTL Variables }}
        {# Single Line Comment #}
        {% comment %}
            Multi Line Comment
        {% endcomment %}
'''
