from django.db import models

# Create your models here.
from django.contrib.auth.models import User


class Account(User):
    about = models.TextField(blank=True, null=True)
    image = models.ImageField( upload_to='account/', blank=True, null=True)


    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
