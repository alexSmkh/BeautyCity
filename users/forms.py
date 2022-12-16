from django import forms

from phonenumber_field.formfields import PhoneNumberField
from .models import UserToCall


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
