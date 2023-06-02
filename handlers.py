import requests
from settings import URL
from messages import (
    START_MESSAGE,
    PARTNER_MESSAGE
)
from buttons import (
    START_KEYBOARD,
    PRODUCT_KEYBOARD,
    INFO_KEYBOARD
)


def get_last_update():
    url = URL + 'getUpdates'
    r = requests.get(url)
    return r.json()['result'][-1]


def start(chat_id, first_name):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': START_MESSAGE.format(first_name),
        'parse_mode': 'HTML',
        'reply_markup': {
            'keyboard': START_KEYBOARD,
            'resize_keyboard': True
        }
    }
    requests.post(url, json=data)
def product(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': "Kerakli bo'limni tanlang👇🏻",
        'reply_markup': {
            'keyboard': PRODUCT_KEYBOARD,
            'resize_keyboard': True
        }
    }
    requests.post(url,json=data)
def info(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': "Kerakli bo'limni tanlang👇🏻",
        'reply_markup': {
            'keyboard': INFO_KEYBOARD,
            'resize_keyboard': True
        }
    }
    requests.post(url,json=data)
def savat(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': "Sizning savatingiz bo'sh",
        'reply_markup': {
            'keyboard':[
                ["🏠 Bosh menyu"]
            ],
            'resize_keyboard': True
        }
    }
def partner(chat_id):
    url = URL + 'sendMessage'
    data = {
        'chat_id': chat_id,
        'text': PARTNER_MESSAGE,
        'reply_markup': {
            'keyboard':[
                ["🏠 Bosh menyu"]
            ],
            'resize_keyboard': True
        }
    }