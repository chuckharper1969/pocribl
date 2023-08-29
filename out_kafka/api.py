from rest_framework import viewsets, permissions
from .serializers import KafkaOutputSerializer
from .models import KafkaOutput


class KafkaOutputViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.IsAuthenticated
    ]

    serializer_class = KafkaOutputSerializer

    def get_queryset(self):
        return self.request.user.out_kafka.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
