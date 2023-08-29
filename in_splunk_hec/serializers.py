from rest_framework import serializers
from .models import SplunkHECInput

class SplunkHECInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SplunkHECInput
        fields = "__all__"
        #read_only_fields = ('input_id','owner',)