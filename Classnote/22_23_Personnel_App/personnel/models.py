from django.db import models
from django.contrib.auth.models import User   
   #fixModel
class FixModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    #user = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
   

   #Models
GENDERS = (
    ('F', 'Fmale'),
    ('M', 'Male'),
    ('O', 'Other'),   

)    

TITLES = (
    (1, 'TeamLead'),
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
    started = models.DateTimeField()
    is_active = models.BooleanField(default=True)  
    ended = models.DateTimeField(blank=True, null=True)


    def __str__(self):
        return f'{self.department}-{self.first_name}- {self.last_name}'


