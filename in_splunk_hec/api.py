from rest_framework import viewsets, permissions
from .serializers import SplunkHECInputSerializer

class SplunkHECInputViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = SplunkHECInputSerializer

    def get_queryset(self):
        return self.request.user.in_splunk_hec.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
