from django.db import models
from django.contrib.auth.models import User


class SplunkHECInput(models.Model):
    owner = models.ForeignKey(User, related_name="in_splunk_hec", on_delete=models.CASCADE, null=True)
    token = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=100)
    index = models.CharField(max_length=100)
    sourcetype = models.CharField(max_length=100, default="splunk_hec")
    status = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.description
