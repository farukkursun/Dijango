from django.db import models

class Student(models.Model):
    first_name= models.CharField(max_length=64, default='')
    last_name= models.CharField(max_length=64, default='')
    number=models.IntegerField(default=0)
    about= models.TextField(default='', null=True, blank=True)
    exists= models.BooleanField(null=True, blank=True)
    date= models.DateField(null=True, blank=True)
    email= models.EmailField(null=True, blank=True)
    avatar= models.ImageField(null=True, blank=True, upload_to='images/')
   


# defoult print ayarlari degistirme
    def __str__(self):
        return f'{self.number} - {self.first_name} {self.last_name}'


# modelin varsayilan özelliklerini degistirmek icin kullanilir

    class Meta:
        ordering=['number']
        verbose_name='ögrenci' #model ismi
        verbose_name_plural='ogrenciler' #modelin cogul ismi
    
