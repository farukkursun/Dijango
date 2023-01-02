from rest_framework import routers
from .views import (
    BlogCategoryView,
    BlogPostView,
    BlogCommentView,
)

router = routers.DefaultRouter()
router.register('categories', BlogCategoryView)
router.register('posts', BlogPostView)
router.register('comments', BlogCommentView)

'''
urlpatterns = [
    path('', include(router.urls))
]
'''

urlpatterns = router.urls

