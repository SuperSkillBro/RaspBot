import config
import telebot
import datetime

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.send_message(message.chat.id, "Для получения актуально расписания отправь /rasp")

@bot.message_handler(commands= ['rasp'])
def rasp(message):
    bot.send_message(message.chat.id, "Привет! Вот актуальное расписание на сегодня: ")
    now = datetime.datetime.now()
    curr_path = str(os.getcwd())
    if now.month < 10:
        g = '0' + str(now.month)
        filename = curr_path + '/bd/' + str(now.day) + '.' + g + '.png'
    else:
        filename = curr_path + '/bd/' + str(now.day) + '.' + str(now.month) + '.png'
    photo = open(filename, 'rb')
    bot.send_photo(message.chat.id, photo)

bot.polling()
