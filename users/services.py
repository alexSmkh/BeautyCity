import random

from django.core.cache import cache

import requests
from environs import Env

env = Env()
env.read_env()


class TelegramMessageSender:
    _TOKEN = env('TG_TOKEN')
    _CHAT_ID = env('TG_CHAT_ID')

    @classmethod
    def send_message(cls, message):
        url = f'https://api.telegram.org/bot{cls._TOKEN}/sendMessage'

        try:
            response = requests.post(
                url,
                data={
                    'chat_id': cls._CHAT_ID,
                    'text': message,
                }
            )
            response.raise_for_status()
        except Exception as e:
            return None


class VerificationCodeBuilder:
    @classmethod
    def create_verification_code(cls, key, expiration_time=300):
        code = random.randint(1000, 9999)
        cache.set(key, code, expiration_time)
        return code

    @classmethod
    def is_code_valid(cls, key, code):
        valid_code = cache.get(key)
        return valid_code == code

    @classmethod
    def is_code_expired(cls, key):
        return bool(cache.get(key))
