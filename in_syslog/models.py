from django.db import models
from django.contrib.auth.models import User


class SyslogInput(models.Model):
    owner = models.ForeignKey(User, related_name="in_syslog", on_delete=models.CASCADE, null=True)
    input_id = models.CharField(max_length=100, unique=True)
    udp_port = models.IntegerField(default=0)
    tcp_port = models.IntegerField(default=0)
    message = models.CharField(max_length=100, blank=True, default="Onboarding")
    status = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.input_id
