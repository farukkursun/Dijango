from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=64, default='')
    last_name = models.CharField(max_length=64, default='')
    number = models.IntegerField(default=0)

# python manage.py makemigrations
# python manage.py migrate

