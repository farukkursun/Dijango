from django.db import models

from django.contrib.auth.models import User
from personnel.models import Personnel

# Extending User Model:
class Account(User):
    about = models.TextField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='account/') # install pillow

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
