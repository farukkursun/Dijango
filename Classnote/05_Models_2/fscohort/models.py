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
# https://docs.djangoproject.com/en/4.1/ref/models/options/#model-meta-options
        # db_table = 'ogrenci' # tablo_adı değiştir.
    class Meta:
        ordering=['number']
        verbose_name='ögrenci' #model ismi
        verbose_name_plural='ogrenciler' #modelin cogul ismi
    


# ! Bir model eklendiğinde/değiştirildiğinde aşağıdaki komutları unutmuyoruz:
# $ python manage.py makemigrations
# $ python manage.py migrate

'''
    # Django - Shell + ORM
    # https://docs.djangoproject.com/en/4.1/ref/models/querysets/#field-lookups
    $ python manage.py shell
    > from fscohort.models import Student
    > objname = Student.objects.create(first_name='Abc', last_name='Def', number=5) # Yeni Kayıt
    > objname = Student.objects.all() # Tüm kayıtları getir (liste)
    > objname = Student.objects.get(number=5) # Number=5 olan kaydı getir (tek kayıt)
    > objname = Student.objects.filter(number=5) # Number=5 olan kayıtları getir (liste)
    > objname = Student.objects.filter(first_name__startswith='Q') # firstname 'Q' ile başlayan kayıtları getir (liste)
    > objname = Student.objects.filter(last_name__endswith='n') # lastname 'n' ile biten kayıtları getir (liste)
    > objname = Student.objects.filter(last_name__contains='a') # lastname 'a' içeren kayıtları getir (liste)
    > objname = Student.objects.exclude(number=5) # Number=5 olMAyan kayıtları getir (liste)
    > objname = Student.objects.exclude(last_name__contains='a') # lastname 'a' içerMEyen kayıtları getir (liste)
    > objname = Student(first_name='Abc', last_name='Def', number=5) # DB'den bağımsız instance (obje)
    > objname.save() # tek kayıt olarak gelen objeyi veritabanına ekler veya günceller.

'''