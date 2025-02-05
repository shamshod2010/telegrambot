import telebot
import ismlar

TOKEN = "8194456682:AAHnrpQOI0ref_AP1p4sQEOmqBalFVfwj64"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Salom! Men oddiy Telegram botman.")

@bot.message_handler(func=lambda msg: True)
def echo(message):
    ism = message.text
    javob = ism.title() + ' ismining manosi: \n' + ismlar.ism_manosi(ism)
    bot.reply_to(message, javob)
bot.polling()
