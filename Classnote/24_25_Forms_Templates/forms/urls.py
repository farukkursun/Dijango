from django.urls import path
from .views import *

urlpatterns = [
    path('view_simple/', view_simple, name='name_view_simple'),
    path('view_template/', view_template, name='view_template'),
    path('view_template_form/', view_template_form, name='view_template_form'),
    path('view_template_form_model/', view_template_form_model, name='view_template_form_model'),
    # CRUD Operations:
    path('form_list/', form_list, name='form_list'),
    path('form_create/', form_create, name='form_create'),
    path('form_update/<int:id>', form_update, name='form_update'),
    path('form_delete/<int:id>', form_delete, name='form_delete'),
]