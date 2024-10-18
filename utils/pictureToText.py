import pytesseract
from PIL import Image


def image_to_text(image_path):

    image = Image.open(image_path)
    
    custom_config = r'-l eng+rus --psm 6'
    text = pytesseract.image_to_string(image, config=custom_config)
    
    print(text)

    return text