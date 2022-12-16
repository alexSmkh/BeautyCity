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
