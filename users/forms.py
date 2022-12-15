from django import forms
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
