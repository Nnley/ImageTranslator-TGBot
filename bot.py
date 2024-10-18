import os

import requests
import telebot
from telebot import types

from utils.deepl import translate
from utils.pictureToText import image_to_text

from config import load_environment_variables
load_environment_variables()


bot = telebot.TeleBot(os.getenv('BOT_TOKEN') or '')

@bot.message_handler(commands=['start'])
def start_handler(message):
    bot.send_message(message.chat.id, 'Хай отправь фото заебал')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):    
    photo_info = message.photo[-1]
    photo_id = photo_info.file_id
    photo_file = bot.get_file(photo_id)
    photo_url = f'https://api.telegram.org/file/bot{bot.token}/{photo_file.file_path}'
    user_id = message.from_user.id
    text = save_photo(photo_url, user_id).replace('\n', ' ')
    translated_text = translate(text)
    
    bot.send_message(user_id, translated_text)


def save_photo(photo_url, user_id):
    response = requests.get(photo_url)
    filename = f'{user_id}.jpg'
    with open(f"img/{filename}", "wb") as f:
        f.write(response.content)
    text = image_to_text(f"img/{filename}")
    os.remove(f"img/{filename}")
    return text
    
    
if __name__ == '__main__':
    bot.polling()