# Generated by Django 3.2.10 on 2022-12-15 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usertocall'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='usertocall',
            name='question',
            field=models.TextField(blank=True, verbose_name='Вопрос'),
        ),
    ]