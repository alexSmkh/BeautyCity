from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
     phonenumber = PhoneNumberField(
        'Номер телефона',
    )
    
