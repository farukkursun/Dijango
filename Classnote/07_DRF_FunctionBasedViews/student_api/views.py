from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet

from django.shortcuts import get_object_or_404

from .models import Student
from .serializers import StudentSerializer

# Temel API görüntüleme

@api_view()
def home(request):
    return Response({
        'message':'hello word'
    })


#------------------------------------------------------
# HTPP Request Type
'''
GET-> public veriler, listeleme, görüntüleme kullanilir
POST-> private veriler. Kayit olusturma islerinde(id ihtiyac duymaz)
PUT -> Post dan türemistir. Kayit güncelleme. veri bütünüyle güncellenir.
PATCH-> Kayit güncelleme. ilgilgi kisim güncellenir.
DELETE->Post dan türemistir.  Kayit silme
'''
#------------------------------------------------------
# Student Serializeers  görüntüleme




'''
@api_view(['GET']) # Default olarak [GET]
def student_list(request):
    students= Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)


#------------------------------------------------------

#yeni kayit ekleme

@api_view(['POST'])
def student_create(request):
    serializer= StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            'message':'Created Successfully'
        },status= status.HTTP_201_CREATED)
    else:
        # return Response({"message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)
        # return Response({
        #     'message': 'Data not Validet'
        # })    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#------------------------------------------------------
# tek kayit görüntüleme

@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

#------------------------------------------------------
# güncelleme
@api_view(['PUT'])
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(data=request.data, instance=student)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Created Successfully"
        }, status.HTTP_201_CREATED)
    else:
        return Response({"status": False, "message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)
        






#------------------------------------------------------
# silme
@api_view(['DELETE'])
def student_delete(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except:
        return Response({'status':False, 'message': 'Not Found'}) 
    else:
        student.delete()
        return Response({
        'status': True,
        'message':"Deleted Successfully"
        }, status.HTTP_204_NO_CONTENT)





#------------------------------------------------------
# Benzer fonksiyonlaru birlestirme
@api_view(['GET','POST'])
def student_list_create(request):
    if request.method== 'GET':
        #listeleme
        students= Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


    elif request.method =='POST':
        #yeni kayit
        serializer= StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
            'message':'Created Successfully'
            }, status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)

#------------------------------------------------------
#görüntüleme,  güncelleme, silme

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):
    try:
        student = Student.objects.get(id=pk)
    except:
         return Response({"status": False, "message": "Not Found"})
    else:

        if request.method == 'GET':
         # Kayıt Görüntüle:
        # student = Student.objects.get(id=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
    
        elif request.method == 'PUT':
         # Kayıt Güncelleme:
        # student = Student.objects.get(id=pk)
            serializer = StudentSerializer(data=request.data, instance=student)
            if serializer.is_valid():
                serializer.save()
                return Response({
                "status": True,
                "message": "Created Successfully"
                }, status.HTTP_201_CREATED)
            else:
                return Response({"status": False, "message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
         # Kayıt Silme:
        # student = Student.objects.get(id=pk)
            student.delete()
            return Response({
            "status": True,
            "message": "Deleted Successfully"
            }, status.HTTP_204_NO_CONTENT)

'''




############################################################



class StudentListCreate(APIView):
    def get(self, ruquest):
        students= Student.objects.all()
        serializer = StudentSerializer(students, many= True)
        return Response(serializer.data)
    def post(self, request):
        serializer =StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)



class StudentDetail(APIView):

    def get_obj(self,pk):
        return get_object_or_404(Student, pk=pk)


    def get(self, request,pk):
        student=self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request,pk):
        student=self.get_obj(pk)
        serializer=StudentSerializer(data=request.data, instance=student)  
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request,pk):
        student=self.get_obj(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    



############################################


class StudentGAV(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    GenericAPIView
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class StudentDetailGAV(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericAPIView
):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)




#########################################################


class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 



####################################################################


class StudentMVS(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer 

    @action(detail=False, methods=['GET'])
    def student_count(self, request):
        count ={
            'student-count':self.queryset.count()
        }
        return Response(count)

