
from django.urls import path, include
from .views import (
    home,
    todo_list_create,
    todo_get_del_upd,
    Todos,
    TodoDetail
    )


urlpatterns = [
   
    path('', home),
    path('todos/', todo_list_create),
    path('todos/<int:id>', todo_get_del_upd),
    path('todos_cls/', Todos.as_view()),
    path('todos_cls/<int:pk>', TodoDetail.as_view()),
]
