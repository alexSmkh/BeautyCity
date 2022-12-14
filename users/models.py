from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class Feedback(models.Model):
    feedback_text = models.TextField(
        'Текст'
    )


class User(AbstractUser):
    phonenumber = PhoneNumberField(
        'Номер телефона'
     )
    feedbacks = models.ForeignKey(
        Feedback,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
