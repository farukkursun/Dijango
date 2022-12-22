from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name=models.CharField(max_length=40)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.name}'


class Post(models.Model):
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=100)
    content=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title} '


class Comment(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=40)
    comment=models.TextField()
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    created_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} '





