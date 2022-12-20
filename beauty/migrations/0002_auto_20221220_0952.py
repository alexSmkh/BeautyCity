# Generated by Django 3.2.10 on 2022-12-20 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='аватар'),
        ),
        migrations.AlterField(
            model_name='procedure',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='картинка'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Картинка'),
        ),
    ]
