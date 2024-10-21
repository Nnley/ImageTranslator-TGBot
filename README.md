# Telegram Bot for Image Text Translation
## What it Does

- **Extract Text from Images**: The bot can recognize and extract text from uploaded images.
- **Translate Text**: The bot can translate text between Russian and English (Russian -> English and English -> Russian).

## Installation

To install the required dependencies, run the following command:

```bash
pip install -r requirements.txt
```

### Dependencies

The project uses the following libraries:

- **Pillow**: A library for image processing.
- **pyTelegramBotAPI**: A library for interacting with the Telegram Bot API.
- **pytesseract**: An interface for using Tesseract OCR.
- **python-dotenv**: A library for working with environment variables.
- **Requests**: A library for making HTTP requests.
- **vkbottle**: A library for working with the VK API (if required).

### Configuration

Fill in the `.env.example` file with your tokens and API keys, and then rename it to `.env.local`.

Make sure you have Tesseract OCR installed. You can find installation instructions [here](https://tesseract-ocr.github.io/tessdoc/Installation.html).
 
If necessary, install the language packs for Tesseract. While it's usually not required for English, it may be needed for other languages.

### Usage

Run the bot:

```bash
python bot.py
```

You're all set! You can now send the bot an image with the text you want to translate. The bot will process the image, extract the text, and translate it into English, sending the result back to you.

### License

This project is licensed under the MIT License. For more details, please see the [LICENSE](LICENSE) file.
