from django.shortcuts import render

from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib import messages

from django.views.generic import (
    ListView, 
    DetailView, 
    CreateView,
    UpdateView,
    DeleteView,
)


class TodoListView(ListView):
    model = Todo
    # template_name = 'todo_list.html' # default template = modelname/modelname_list.html


class TodoDetailView(DetailView):
    model = Todo
    

class TodoCreateView(CreateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('index') # işlem bittikten sonra yönlendirilecek adres.
    # template_name = 'todo_form.html' # default template = modelname/modelname_form.html

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Kaydedildi.')
        return super().post(request, *args, **kwargs)


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy('index')

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Güncellendi.')
        return super().post(request, *args, **kwargs)


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy('index')
    template_name = 'todo/todo_delete.html'

    def post(self, request, *args, **kwargs):
        messages.success(request, 'Silindi.')
        return super().post(request, *args, **kwargs)
