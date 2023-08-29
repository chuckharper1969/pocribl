from rest_framework import viewsets, permissions
from .serializers import SyslogInputSerializer
from .models import SyslogInput


class SyslogInputViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = SyslogInputSerializer

    def get_queryset(self):
        return self.request.user.in_syslog.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
