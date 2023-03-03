
from django.urls import path
from .views import home,order, edit_order, pizzas
urlpatterns = [
    
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('order/<int:pk>', edit_order, name='edit_order'),
    path('pizzas/', pizzas, name='pizzas')
]
