import telebot
import os
from flask import Flask, request

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHANNEL_ID = os.environ.get("CHANNEL_ID")

bot = telebot.TeleBot(BOT_TOKEN)
app = Flask(__name__)

@app.route('/')
def index():
    return "Bot is running."

@app.route('/' + BOT_TOKEN, methods=['POST'])
def getMessage():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return 'ok', 200

@bot.message_handler(func=lambda message: True)
def relay_message(message):
    if message.from_user and message.from_user.username == "3commas_notifications_bot":
        bot.send_message(CHANNEL_ID, message.text)

# Запуск через webhook
def run():
    bot.remove_webhook()
    bot.set_webhook(url=os.environ.get("RENDER_EXTERNAL_URL") + '/' + BOT_TOKEN)

if name == '__main__':
    run()
    app.run(host="0.0.0.0", port=10000)
