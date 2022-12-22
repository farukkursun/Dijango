from django.shortcuts import render
from django.http.response import HttpResponse

from .models import Category, Post, Comment
from .serilaziers import CategorySerializers, PostSerializers, CommentSerializers

from rest_framework.viewsets import ModelViewSet

from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly

def home(request):
    return HttpResponse(
        '<center><h1 style="background-color:powderblue;">Welcome to Blogapp</h1></center>'
    )


class PostMVS(ModelViewSet):
    queryset =Post.objects.all()
    serializer_class=PostSerializers
    permission_classes= [IsAuthenticatedOrReadOnly]


class CommentMVS(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers
    permission_classes= [IsAuthenticated]

class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
    permission_classes= [IsAdminUser]
