from rest_framework import routers
from .api import StudentViewSet

router = routers.DefaultRouter()
router.register('api/studentlists', StudentViewSet, 'studentlists')

urlpatterns = router.urls
