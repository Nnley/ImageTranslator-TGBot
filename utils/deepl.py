import os
import json

import requests

from config import load_environment_variables
load_environment_variables()


def translate(text):
    auth_key = os.getenv('DEEPL_KEY') or ''
    
    target_lang = check_language(text)
    print(target_lang)
    url = 'https://api-free.deepl.com/v2/translate'
    payload = {
        'auth_key': auth_key,
        'text': text,
        'target_lang': target_lang,
    }
    response = requests.post(url, data=payload)
    print(response.json())
    
    translation = json.loads(response.content.decode('utf-8'))['translations'][0]['text']
    print(translation)
    return translation

def check_language(text):
    rus_letters = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    eng_letters = set('abcdefghijklmnopqrstuvwxyz')
    rus_count = 0
    eng_count = 0
    for char in text.lower():
        if char in rus_letters:
            rus_count += 1
        elif char in eng_letters:
            eng_count += 1
    if rus_count > eng_count:
        return 'EN'
    else:
        return 'RU'