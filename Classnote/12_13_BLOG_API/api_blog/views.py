from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *
from .permissions import (IsAdminOrReadOnly, IsOwnerOrAdminOrReadOnly)

# -------------------- FixView --------------------------------------

class FixView(ModelViewSet):
    pass

# -------------------- Views --------------------------------------

class BlogCategoryView(FixView):
    queryset = BlogCategory.objects.all()
    serializer_class = BlogCategorySerializer
    permission_classes = [IsAdminOrReadOnly] # Herkes görebilir veya sadece Admin


class BlogPostView(FixView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly] # Herkes görebilir veya sadece (Admin veya Sahibi)

    # Override -> Her görüntüleme için viewed sayacını 1 arttır.
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object() # Obje verisi al.
        instance.viewed += 1 # viewed 1 arttır.
        instance.save() # objeyi kaydet.
        return super().retrieve(request, *args, **kwargs) # Orjinal methodu çalıştır.


class BlogCommentView(FixView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly] # Herkes görebilir veya sadece (Admin veya Sahibi)