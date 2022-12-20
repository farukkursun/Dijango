# -------------------------------------------------------------------
#    DRF - Function Based Views
# -------------------------------------------------------------------
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView, mixins, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from django.shortcuts import get_object_or_404

from .serializers import StudentSerializer
from .models import Student

# Temel API görüntüleme:


@api_view()
def home(request):
    return Response({
        "message": "Hello World"
    })


# -------------------------------------------------------------------
'''
    HTTP Request Types:
        GET -> Public verilerdir. Listeleme/Görüntüleme işlemlerinde kullanılır.
        POST -> Private verilerdir. Kayıt oluşturma işlemlerinde kullanılır. (ID'ye ihtiyaç duymaz.)
        * PUT -> Kayıt güncelleme işlemlerinde kullanılır. (Veri bir bütün olarak güncellenir.) (ID'ye ihtiyaç duyar.)
        * PATCH -> Kayıt güncelleme işlemlerinde kullanılır. (Verinin sadece ilgili kısmı güncellenir.) (ID'ye ihtiyaç duyar.)
        * DELETE -> Kayıt silme işlemlerinde kullanılır. (ID'ye ihtiyaç duyar.)
'''

# ------------------------ FBV ------------------------------------

'''
# -------------------------------------------------------------------
# StudentSerializers Tüm Kayıtlar Görüntüleme:


@api_view(['GET'])  # Default: ['GET']
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

# -------------------------------------------------------------------
# StudentSerializers Yeni Kayıt Ekleme:


@api_view(['POST'])
def student_create(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "message": "Created Successfully"
        }, status=status.HTTP_201_CREATED)
    else:
        # return Response({"message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)
        # return Response({"message": "Data not Validated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# -------------------------------------------------------------------
# StudentSerializers Tek Kayıt Görüntüleme:

@api_view(['GET'])
def student_detail(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(student)
    return Response(serializer.data)

# -------------------------------------------------------------------
# StudentSerializers Tek Kayıt Güncelleme:


@api_view(['PUT'])
def student_update(request, pk):
    student = Student.objects.get(id=pk)
    serializer = StudentSerializer(data=request.data, instance=student)
    if serializer.is_valid():
        serializer.save()
        return Response({
            "status": True,
            "message": "Updated Successfully"
        }, status=status.HTTP_202_ACCEPTED)
    else:
        return Response({"status": False, "message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------------------
# StudentSerializers Tek Kayıt Silme:


@api_view(['DELETE'])
def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.delete()
    return Response({
        "status": True,
        "message": "Deleted Successfully"
    }, status=status.HTTP_204_NO_CONTENT)

# -------------------------------------------------------------------
# -------------------------------------------------------------------
# Benzer Fonksiyonları Birleştirelim:
# -------------------------------------------------------------------
# -------------------------------------------------------------------
# Kayıtlar Listeleme + Yeni Kayıt


@api_view(['GET', 'POST'])
def student_list_create(request):
    if request.method == 'GET':
        # Listeleme:
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Yeni Kayıt:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Created Successfully"
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)

# -------------------------------------------------------------------
# Kayıt Görüntüleme + Güncelleme + Silme:


@api_view(['GET', 'PUT', 'DELETE'])
def student_detail_update_delete(request, pk):

    try:
        # Dene:
        student = Student.objects.get(id=pk)
    except:
        # Hata verirse çalıştır:
        return Response({"status": False, "message": "Not Found"})
    else:
        # Hata vermez ise çalıştır:
        if request.method == 'GET':
            # Kayıt Görüntüle:
            serializer = StudentSerializer(student)
            return Response(serializer.data)

        elif request.method == 'PUT':
            # Kayıt Güncelleme:
            serializer = StudentSerializer(data=request.data, instance=student)
            if serializer.is_valid():
                serializer.save()
                return Response({
                    "status": True,
                    "message": "Updated Successfully"
                }, status=status.HTTP_202_ACCEPTED)
            else:
                return Response({"status": False, "message": "Data not Validated", "data": serializer.data}, status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            # Kayıt Silme:
            student.delete()
            return Response({
                "status": True,
                "message": "Deleted Successfully"
            }, status=status.HTTP_204_NO_CONTENT)
'''

# ----------------------- CBV -------------------------------------


class StudentListCreate(APIView):

    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, requset):
        serializer = StudentSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetail(APIView):

    def get_obj(self, pk):
        return get_object_or_404(Student, pk=pk)

    def get(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_obj(pk)
        serializer = StudentSerializer(data=request.data, instance=student)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_obj(pk)
        student.delete()
        data = {
            'message': 'Student succesfully deleted.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

##################### Generic APIView ###########################


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


######### Concrete Views ############


class StudentCV(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailCV(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


############ ModelViewSet #############
from .pagination import (
    CustoppageNumberPagination,
    CustomLimitOffsetPagination,
    CustumCurserPagination,
)


from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class StudentMVS(ModelViewSet):
    queryset = Student.objects.all().order_by('-id')
    serializer_class = StudentSerializer
    pagination_class= CustoppageNumberPagination #pgn ayyarlari
    # pagination_class=CustomLimitOffsetPagination
    # pagination_class= CustumCurserPagination
    filter_backends=[DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields= [ 'id', 'number','first_name']
    search_fields = ['first_name', 'last_name'] # içinde (LIKE '%%') arama yapar.
    ordering_fields= ['id', 'first_name', 'last_name', 'number']

    @action(detail=False, methods=['GET'])
    def student_count(self, request):
        count = {
            'student-count': self.queryset.count()
        }
        return Response(count)

    @action(detail=True, methods=['GET'])
    def check_student(self, request, pk):
        student = get_object_or_404(Student, pk=pk)
        if student.first_name.startswith('j'):
            return Response({'a': 'aaaaa'})
        return Response({'b': 'bbbbb'})
