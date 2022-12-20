from django import forms

from .models import Appointment


class AppointmentForm(forms.ModelForm):

    class Meta:
        model = Appointment
        field = ('procedure', 'employee', 'salon', 'appointment_hour', 'date')