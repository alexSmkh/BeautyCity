# Generated by Django 3.2.10 on 2022-12-15 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0002_auto_20221215_1148'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказчик', 'verbose_name_plural': 'Заказчики'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Атрибуты заказа', 'verbose_name_plural': 'Атрибуты '},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=25, verbose_name='Категория'),
        ),
    ]
