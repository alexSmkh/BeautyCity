# Generated by Django 3.2.10 on 2022-12-15 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salon',
            name='procedure_categories',
        ),
    ]