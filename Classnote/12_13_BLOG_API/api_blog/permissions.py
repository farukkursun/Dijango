from rest_framework import permissions

# -------------------- Permissions --------------------------------------

# Herkes görebilir. Sadece Admin -> ekle/düzenle/sil:
class IsAdminOrReadOnly(permissions.BasePermission):
    # Genel İzin Kontrol:
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_staff


# Herkes görebilir. Sadece Admin veya Sahibi -> ekle/düzenle/sil:
class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    # Her bir kayda (objeye) özel izin kontrol:
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            # Admin or Creator
            return request.user.is_staff or obj.user == request.user