from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404

from rest_framework.response import Response 
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
# Create your views here.
from .models import Todo
from .serializers import TodoSerializers

def home(request):
    return HttpResponse(
       '<center><h1 style="background-color:powderblue;">Welcome to ApiTodo</h1></center>' 
    )


@api_view(['GET','POST'])
def todo_list_create(request):
   if request.method == 'GET':
      todos= Todo.objects.all()
      serializer=TodoSerializers(todos, many=True)
      return Response(serializer.data)
   elif request.method ==  'POST':
      serializer=TodoSerializers(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET', 'PUT', 'DELETE'])
def todo_get_del_upd(request, id):
   todo = get_object_or_404(Todo, id=id)
   if request.method == 'GET':
      
      sserializer = TodoSerializers(todo)
      return Response(sserializer.data)
   

   elif request.method == 'PUT':
      sserializer= TodoSerializers(data=request.data, instance=todo)
      if sserializer.is_valid():
         sserializer.save()
         return Response(sserializer.data, status=status.HTTP_202_ACCEPTED)
      return Response(sserializer.errors, status=status.HTTP_400_BAD_REQUEST)
   elif request.method =='DELETE':
      todo.delete()
      return Response({'message': 'todo deleted...'})




class Todos(ListCreateAPIView):
   queryset = Todo.objects.all()
   serializer_class= TodoSerializers



class TodoDetail(RetrieveUpdateDestroyAPIView):
   queryset = Todo.objects.all()
   serializer_class= TodoSerializers  