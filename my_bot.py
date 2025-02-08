import telebot
import time
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)
stop_flag = False


def stop_bot():
    global stop_flag
    stop_flag = True


@bot.message_handler(func=lambda message: 'send me your photo please' in message.text.lower())
def send_image(message):
    image_path = "photo_3.jpg"
    with open(image_path, 'rb') as photo:
        time.sleep(30)
        bot.send_photo(message.chat.id, photo, caption="Как я выгляжу?")


@bot.message_handler(commands=['stop'])
def stop_command(message):
    bot.stop_polling()


@bot.message_handler()
def info(message):
    if message.text.lower() == "привет":
        time.sleep(5)
        bot.send_message(message.chat.id, "Привет!")
    elif message.text.lower() == "как дела?":
        time.sleep(10)
        bot.send_message(message.chat.id, "Супер! У тебя как?")
    elif message.text.lower() == "чем занимаешься?":
        time.sleep(40)
        bot.send_message(message.chat.id, "Особо ничем фильм смотрю")
    elif message.text.lower() == "давай куда-нибудь сходим":
        time.sleep(50)
        bot.send_message(message.chat.id, "Можно а куда?")
    elif message.text.lower() == "давай в кальянную на ленина":
        time.sleep(5)
        bot.send_message(message.chat.id, "давай только ко мне подруга сейчас должна прийти")
    elif message.text.lower() == "бери ее с собой веселее будет":
        time.sleep(10)
        bot.send_message(message.chat.id, "Ну не знаю, если согласиться")
    elif message.text.lower() == "я думаю согласиться скажи ей я для нее кого-нибудь позову":
        time.sleep(15)
        bot.send_message(message.chat.id, "Ладно попробую")
    elif message.text.lower() == "давай я через час заеду нормально будет":
        time.sleep(5)
        bot.send_message(message.chat.id, "Да давай отлично")
    elif message.text.lower() == "ок договорились)":
        time.sleep(5)
        bot.send_message(message.chat.id, "целую и жду)")


def polling():
    global stop_flag
    while not stop_flag:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(5)


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True)
    except KeyboardInterrupt:
        print("Bot stopped manually.")
