from rest_framework import routers
from .api import SyslogInputViewSet

router = routers.DefaultRouter()
router.register('', SyslogInputViewSet, 'in_syslog')

urlpatterns = router.urls
