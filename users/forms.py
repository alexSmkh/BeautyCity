from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from phonenumber_field.formfields import PhoneNumberField

from .models import UserToCall, User


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('phonenumber',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('phonenumber',)


class UserToCallForm(forms.ModelForm):

    class Meta:
        model = UserToCall
        fields = ('name', 'phonenumber', 'question')
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Введите имя', 'class': 'contacts__form_iunput',}),
            'phonenumber': forms.TextInput(attrs={'placeholder': 'Введите номер телефона', 'class': 'contacts__form_iunput'}),
            'question': forms.Textarea(attrs={'placeholder': 'Введите вопрос (необязательно)', 'class': 'contacts__form_textarea'})
        }


class RequestRegistrationCodeForm(forms.Form):
    phonenumber = PhoneNumberField(region='RU')
    confirm_rules = forms.BooleanField()


class ConfirmRegistrationForm(forms.Form):
    phonenumber = PhoneNumberField(region='RU')
    code = forms.IntegerField()
