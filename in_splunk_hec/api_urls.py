from rest_framework import routers
from .api import SplunkHECInputViewSet

router = routers.DefaultRouter()
router.register('', SplunkHECInputViewSet, 'in_splunk_hec')

urlpatterns = router.urls
