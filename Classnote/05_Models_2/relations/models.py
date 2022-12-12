from django.db import models

class Account(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    email = models.EmailField()

    def __str__(self):
        return f'{self.username}'

# One to One Relation:
class Profile(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    about = models.TextField()
    # Relation Column
    account = models.OneToOneField(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account} {self.first_name}'

'''
on_delete properties:
    # CASCADE -> if primary deleted, delete foreing too.
    # SET_NULL -> if primary deleted, set foreign to NULL. (null=True)
    # SET_DEFAULT -> if primary deleted, set foreing to DEFAULT value. (default='Value')
    # DO_NOTHING -> if primary deleted, do nothing.
    # PROTECT -> if foreign is exist, can not delete primary.
'''

# Many to One Relation:
class Address(models.Model):
    name = models.CharField(max_length=32)
    address = models.TextField()
    country = models.CharField(max_length=32)
    phone = models.CharField(max_length=32)
    # Relation Column: ForeingKey -> ManyToOne
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.account} {self.address}'

# Many to Many Relation:
class Product(models.Model):
    brand = models.CharField(max_length=32)
    product = models.CharField(max_length=128)
    # Relation Column
    account = models.ManyToManyField(Account) # ManyToMany ilişkide on_delete kullanılmaz.


