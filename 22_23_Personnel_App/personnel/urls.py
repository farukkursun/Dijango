from rest_framework import routers
from .views import DepartmentView, PersonnelView

router = routers.DefaultRouter()
router.register('departments', DepartmentView)
router.register('personnels', PersonnelView)

urlpatterns = router.urls
