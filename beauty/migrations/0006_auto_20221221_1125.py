# Generated by Django 3.2.10 on 2022-12-21 11:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('beauty', '0005_alter_appointment_appointment_hour'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='client_name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='имя клиента'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='question',
            field=models.TextField(blank=True, null=True, verbose_name='вопрос'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to=settings.AUTH_USER_MODEL),
        ),
    ]