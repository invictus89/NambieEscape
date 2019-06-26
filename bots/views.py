from django.shortcuts import render
from django.conf import settings
import requests

# Create your views here.
bot_token = settings.TELEGRAM_BOT_TOKEN
bot_name = settings.TELEGRAM_BOT_NAME
bot_redirect_url = settings.TELEGRAM_LOGIN_REDIRECT_URL

api_url = f'https://api.telegram.org/bot{bot_token}'
webhook_url = 'https://786d1f57.ngrok.io/accounts/'
my_url = f'{api_url}/setWebhook?url={webhook_url}'

def telegram(request, token=None):
    # 1. 사용자 정보 가져오기 위한 요청
    update_url = f'{api_url}/getUpdates'
    response = requests.get(update_url).json()
    # 2. 사용자의 채팅 id 출력
    chat_id = response['result'][0]['message']['from']['id']
    print(chat_id)
    # 3. 메세지 전송
    text = random.sample(range(1, 46), 6)
    send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(send_url)

    