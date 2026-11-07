import os
import telebot

TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "اهلا، البوت شغال ✅")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, "وصلتني: " + message.text)

print("Bot is running...")
bot.infinity_polling()
