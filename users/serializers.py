from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class RequestCodeSerializer(serializers.Serializer):
    phonenumber = PhoneNumberField()


class ConfirmRegistrationSerializer(serializers.Serializer):
    phonenumber = PhoneNumberField()
    code = serializers.IntegerField()
