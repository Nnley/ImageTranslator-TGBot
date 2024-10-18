import os

import requests
from vkbottle.bot import Bot, Message

from utils.deepl import translate
from utils.pictureToText import image_to_text

from config import load_environment_variables
load_environment_variables()


bot = Bot(token=os.getenv('VK_TOKEN') or '')

@bot.on.message(text=["test"])
async def start_handler(message: Message):
    await message.answer("Хуй")

@bot.on.message(attachment=["photo"])
async def photo_handler(message: Message):
    if message.attachments:
        photo = message.attachments[0].photo
        if photo:
            max_size = max(photo.sizes, key=lambda size: size.width)
            url = max_size.url
            user_id = message.from_id
            text = save_photo(url, user_id).replace('\n', '')
            translated_text = translate(text)
            
            await message.answer(translated_text)
    
    
def save_photo(photo_url, user_id):
    response = requests.get(photo_url)
    filename = f'{user_id}.jpg'
    with open(f"img/{filename}", "wb") as f:
        f.write(response.content)
    text = image_to_text(f"img/{filename}")
    os.remove(f"img/{filename}")
    return text

if __name__ == "__main__":
    bot.run_forever()