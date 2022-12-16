from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from .managers import CustomUserManager


class User(AbstractUser):
    phonenumber = PhoneNumberField(
        'Номер телефона',
        unique=True,
        db_index=True,
    )

    USERNAME_FIELD = 'phonenumber'

    objects = CustomUserManager()

    def __str__(self):
        return self.phonenumber

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserToCall(models.Model):

    STATUS = (
        ('raw', 'Необработанный'),
        ('finished', 'Обработанный')
    )

    name = models.CharField(
        'Имя пользователя',
        max_length=50
    )
    phonenumber = PhoneNumberField(
        'Номер телефона'
    )
    question = models.TextField(
        'Вопрос',
        blank=True
    )
    status = models.CharField(
        'Статус звонка',
        max_length=25,
        choices=STATUS,
        default='raw',
        db_index=True
    )

    def __str__(self):
        return f'{self.id} {self.name} {self.phonenumber} {self.get_status_display()}'

    class Meta:
        verbose_name = 'Консультация пользователя'
        verbose_name_plural = 'Консультация пользователей'
