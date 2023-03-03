from django.contrib import admin

# Register your models here.
from .models import Size, Pizza


admin.site.register(Size)
admin.site.register(Pizza)