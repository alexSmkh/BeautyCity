from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):

    def create_user(self, phonenumber, **extra_fields):
        """
        Create and save a User with the given phone number.
        """
        if not phonenumber:
            raise ValueError(_('The phone number must be set'))

        if not phonenumber.is_valid():
            raise ValueError(_('The phone number is not valid'))

        user = self.model(phonenumber=phonenumber, **extra_fields)
        user.save()
        return user
