from django.urls import path, include

# --- FBV IMPORTS -----
'''
from .views import (
    home,
    student_list,
    student_create,
    student_detail,
    student_update,
    student_delete,
    student_list_create,
    student_detail_update_delete,
)
'''

# --- CBV IMPORTS -----
from .views import (
    home,
    StudentListCreate,
    StudentDetail,
    StudentGAV,
    StudentDetailGAV,
    StudentCV,
    StudentDetailCV,
    StudentMVS
)

from rest_framework import routers
router = routers.DefaultRouter()
router.register('student', StudentMVS)

# after /api/:
# ----------- FBV URLS --------------
'''
urlpatterns = [
    path('', home),
    path('student_list/', student_list),
    path('student_create/', student_create),
    path('student_detail/<int:pk>', student_detail),
    path('student_update/<int:pk>', student_update),
    path('student_delete/<int:pk>', student_delete),
    # concat_functions()
    path('student_list_create/', student_list_create),
    path('student_detail_update_delete/<int:pk>', student_detail_update_delete),
]
'''

urlpatterns = [
    path('', home),
    # path('student/', StudentListCreate.as_view()),
    # path('student/', StudentGAV.as_view()),
    # path('student/', StudentCV.as_view()),
    # path('student/<int:pk>/', StudentDetail.as_view())
    # path('student/<int:pk>/', StudentDetailGAV.as_view())
    # path('student/<int:pk>/', StudentDetailCV.as_view())
    path('', include(router.urls))
]
