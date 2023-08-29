from rest_framework import serializers
from .models import KafkaOutput

class KafkaOutputSerializer(serializers.ModelSerializer):
    class Meta:
        model = KafkaOutput
        fields = "__all__"
        read_only_fields = ('output_id','owner',)