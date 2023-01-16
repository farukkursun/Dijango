from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=20, default='')


    

class Personel(models.Model):
    GENDER = (
        (1, 'Female'),
        (2, 'male')
    )
    joined_day = models.IntegerField(default=0)
    first_name = models.CharField(max_length=20, default='')
    last_name = models.CharField(max_length=20, default='')
    is_staffed =models.BooleanField(default=False)
    title = models.CharField(max_length=20, default='')
    gender = models.IntegerField(choices=GENDER, default=1)
    salary = models.IntegerField(default=1000)
    start_date = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department,on_delete=models.CASCADE)


