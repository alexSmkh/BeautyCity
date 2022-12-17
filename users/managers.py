from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.hashers import make_password


class CustomUserManager(BaseUserManager):

    def _create_user(self, phonenumber, password, **extra_fields):
        if not phonenumber:
            raise ValueError(_('The phone number must be set'))

        user = self.model(phonenumber=phonenumber, **extra_fields)

        if password is not None:
            user.password = make_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, phonenumber, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(phonenumber, password, **extra_fields)

    def create_superuser(self, phonenumber, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self._create_user(phonenumber, password, **extra_fields)
