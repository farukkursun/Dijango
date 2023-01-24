
from django.urls import path
from .views import*

urlpatterns = [
    path('view_simple/', view_simple, name='name_view_simple'),
    path('view_template/', view_template, name='view_template'),
    path('view_template_form/', view_template_form, name='view_template_form'),
    path('view_template_form_model/', view_template_form_model, name='view_template_form_model'),
]

from django.conf import settings
from django.conf.urls.static import static
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
