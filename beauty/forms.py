from django import forms

from phonenumber_field.formfields import PhoneNumberField
from django.forms import CharField

from users.models import User
from .models import Appointment


class AppointmentForm(forms.ModelForm):
    phone_number = PhoneNumberField()
    question = CharField()
    client_name = CharField()

    class Meta:
        model = Appointment
        fields = (
            'procedure', 'employee', 'salon', 'appointment_hour', 'date', 'phone_number', 'question', 'client_name'
        )

    def save(self, commit=True):
        appointment = super(AppointmentForm, self).save(commit=False)
        user = User.objects.get(phonenumber=self.cleaned_data['phone_number'])
        appointment.user_id = user.id
        if commit:
            appointment.save()
        return appointment
