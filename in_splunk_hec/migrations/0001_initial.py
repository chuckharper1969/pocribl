# Generated by Django 4.2.4 on 2023-08-29 14:40

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
            name='SplunkHECInput',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=100, unique=True)),
                ('description', models.CharField(max_length=100)),
                ('index', models.CharField(max_length=100)),
                ('sourcetype', models.CharField(default='splunk_hec', max_length=100)),
                ('status', models.IntegerField(default=0)),
                ('modified_at', models.DateTimeField(auto_now_add=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_splunk_hec', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
