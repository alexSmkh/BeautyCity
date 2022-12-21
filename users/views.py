import json
from http import HTTPStatus

from django.http import JsonResponse
from django.contrib.auth import login, logout
from django.shortcuts import redirect


from phonenumber_field.phonenumber import PhoneNumber

from .models import User
from .forms import RequestRegistrationCodeForm, ConfirmRegistrationForm
from .services import TelegramMessageSender, VerificationCodeBuilder


def request_code(request):
    if request.method == 'POST':
        form = RequestRegistrationCodeForm(json.loads(request.body))
        if not form.is_valid():
            return JsonResponse(
                data=form.errors,
                status=HTTPStatus.BAD_REQUEST,
                json_dumps_params={'ensure_ascii': False},
            )

        code = VerificationCodeBuilder.create_verification_code(form.data['phonenumber'])
        TelegramMessageSender.send_message(f'Ваш код: {code}')

        return JsonResponse(data={}, status=HTTPStatus.OK)


def confirm_registration(request):
    if request.method == 'POST':
        form = ConfirmRegistrationForm(json.loads(request.body))

        if not form.is_valid():
            return JsonResponse(
                form.errors,
                status=HTTPStatus.BAD_REQUEST,
                json_dumps_params={'ensure_ascii': False},
            )

        user_phonenumber = form.data['phonenumber']

        if VerificationCodeBuilder.is_code_expired(user_phonenumber):
            errors = {
                'code': ['Код недействителен. Пожалуйста, запросите новый.'],
            }
            return JsonResponse(
                data=errors,
                status=HTTPStatus.BAD_REQUEST,
                json_dumps_params={'ensure_ascii': False},
            )

        user_code = form.data['code']

        if not VerificationCodeBuilder.is_code_valid(user_phonenumber, user_code):
            errors = {
                'code': ['Неправильный код. Пожалуйста, попробуйте еще раз.'],
            }
            return JsonResponse(
                data=errors,
                status=HTTPStatus.BAD_REQUEST,
                json_dumps_params={'ensure_ascii': False},
            )

        user_phonenumber = PhoneNumber.from_string(user_phonenumber)
        user, _ = User.objects.get_or_create(phonenumber=user_phonenumber)
        login(request, user)

        return JsonResponse(
            data={},
            status=HTTPStatus.OK,
        )


def logout_user(request):
    logout(request)
    return redirect('/')
