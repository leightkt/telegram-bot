import os
from telebot import types, TeleBot

BOT_TOKEN = os.environ.get('BOT_TOKEN')
APP_URL = os.environ.get('APP_URL')

button1 = types.InlineKeyboardButton(text="Play Hockey 🏒", url=APP_URL)
button2 = types.InlineKeyboardButton(text="Play Soccer ⚽️", url=APP_URL)
keyboard = types.InlineKeyboardMarkup()
keyboard.add(button1)
keyboard.add(button2)

bot = TeleBot(BOT_TOKEN)
print('starting bot...')

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "Hello! Welcome!")
    bot.send_message(message.chat.id, "What would you like to play?", reply_markup=keyboard)

bot.infinity_polling()