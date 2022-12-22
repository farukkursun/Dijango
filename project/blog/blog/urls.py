from rest_framework import routers


from django.urls import path, include
from .views import (
   home,
   PostMVS,
   CommentMVS,
   CategoryMVS
   
   )


router = routers.DefaultRouter()
router.register('post', PostMVS)
router.register('comment', CommentMVS)
router.register('category',CategoryMVS)



urlpatterns = [
   path('', home),
    path('', include(router.urls)),
]
