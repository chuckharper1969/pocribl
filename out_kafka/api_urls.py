from rest_framework import routers
from .api import KafkaOutputViewSet

router = routers.DefaultRouter()
router.register('', KafkaOutputViewSet, 'out_kafka')

urlpatterns = router.urls
