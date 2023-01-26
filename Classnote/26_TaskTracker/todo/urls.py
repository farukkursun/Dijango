from django.urls import path

# ------------- Function Based Views ------------------
from .views_funcs import *
urlpatterns = [
    path('', todo_list, name="index"),
    path('add/', todo_add, name="todo_add"),
    path('update/<int:pk>', todo_update, name="todo_update"),
    path('delete/<int:pk>', todo_delete, name="todo_delete"),
]

# ------------- Class Based Views ------------------
from .views import *

urlpatterns = [
    path('', TodoListView.as_view(), name="index"),
    path('add/', TodoCreateView.as_view(), name="todo_add"),
    path('detail/<int:pk>', TodoDetailView.as_view(), name="todo_detail"),
    path('update/<int:pk>', TodoUpdateView.as_view(), name="todo_update"),
    path('delete/<int:pk>', TodoDeleteView.as_view(), name="todo_delete"),
]