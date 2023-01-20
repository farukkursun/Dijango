from django.db import models
from django.contrib.auth.models import User

# ----------------- FixModel ------------------

class FixModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# ----------------- Models ------------------

GENDERS = (
    ('F', 'Female'),
    ('M', 'Male'),
    ('O', 'Other'),
)

TITLES = (
    (1, 'Team Lead'),
    (2, 'Personnel'),
)

class Department(FixModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Personnel(FixModel):
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDERS)
    title = models.SmallIntegerField(choices=TITLES)
    salary = models.IntegerField()
    started = models.DateTimeField() # models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    ended = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'[{self.is_active}] {self.department} - {self.first_name} {self.last_name} # {self.user}'
