from django.db import models
from django.contrib.auth.models import User


class KafkaOutput(models.Model):
    owner = models.ForeignKey(User, related_name="out_kafka", on_delete=models.CASCADE, null=True)
    output_id = models.CharField(max_length=100)
    broker = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    message = models.CharField(max_length=100, blank=True, default="Onboarding")
    status = models.IntegerField(default=0)
    modified_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.output_id}/{self.broker}/{self.topic}'
