from flask import Flask, request
import requests
import os

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
TELEGRAM_CHANNEL_ID = os.environ['TELEGRAM_CHANNEL_ID']

@app.route('/', methods=['GET'])
def home():
    return '3Commas Telegram Webhook is Live!'

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json

    message = f"📊 Новое событие от 3Commas:\n\n{data}"

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHANNEL_ID,
        'text': message
    }
    requests.post(url, data=payload)

    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
