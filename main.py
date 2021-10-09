import telebot  # pip install pyTelegramBotAPI
import os

bot = telebot.TeleBot(os.environ.get('BOT_TOKEN'))

# Exemple of an initial command. (/start)


@bot.message_handler(commands=['start'])
def test(message):
    bot.send_message(message.chat.id, "Bem vindo ao meu bot")

# Exemple of a command echoing a massgem provided by the user.


@bot.message_handler(commands=['echo'])
def test(message):
    messageText = message.text.replace("/echo", "")
    bot.send_message(message.chat.id, messageText)

# Exemple of a command sending a picture to the user.


@bot.message_handler(commands=['foto'])
def test(message):
    messageText = message.text.replace("/echo", "")
    bot.send_message(message.chat.id, messageText)
    photo = open('photo.png', 'rb')
    bot.send_photo(message.chat.id, photo)


bot.polling()
