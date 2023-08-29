# Generated by Django 4.2.4 on 2023-08-29 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KafkaOutput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('output_id', models.CharField(max_length=100)),
                ('broker', models.CharField(max_length=100)),
                ('topic', models.CharField(max_length=100)),
                ('message', models.CharField(blank=True, default='Onboarding', max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='out_kafka', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
