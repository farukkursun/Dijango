from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status

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

from .models import Student
from .serializers import StudentSerializer


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
        }, status.HTTP_201_CREATED)
    else:
        return Response({"message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)
        # return Response({
        #     'message': 'Data not Validet'
        # })    

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