import random
import time
from datetime import timedelta

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
    __storage = {}

    @classmethod
    def set(cls, key, value, expire: timedelta):
        cls.__storage[key] = (value, time.time() + expire.total_seconds())

    @classmethod
    def get_code(cls, key):
        values = cls.__storage.get(key)
        if values is None:
            return None
        return values[0]

    @classmethod
    def is_code_expired(cls, code):
        _, expire_at = cls.__storage.get(code)
        return expire_at < time.time()

    @classmethod
    def create_verification_code(cls, key, expiration_time=300):
        code = random.randint(1000, 9999)
        cls.set(key, code, timedelta(seconds=expiration_time))
        return code

    @classmethod
    def is_code_valid(cls, key, code):
        return cls.get_code(key) == code

