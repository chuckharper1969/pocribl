from rest_framework import serializers
from .models import SyslogInput

class SyslogInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = SyslogInput
        fields = "__all__"
        read_only_fields = ('input_id','owner',)