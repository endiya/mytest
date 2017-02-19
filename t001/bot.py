# -*- coding: utf-8 -*-
import telebot
import config
from subprocess import Popen, PIPE
import parser

bot = telebot.TeleBot(config.token)
print (bot.get_me())
#print (bot.get_updates())
html_tag = 'a'
html_tag2 = 'div'
url = "https://yandex.ru"
url2 = "https://lenta.ru/"

sfclass="link link_black_yes b-afisha__item"
sfclass2="b-yellow-box__wrap"
kino = parser.func_find(html_tag,url,sfclass)
print(kino)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Support_Bot!")


@bot.message_handler(commands=['kino'])
def send_kino(message):
    for i in kino:
        bot.send_message(message.chat.id, i)

@bot.message_handler(commands=['kino2'])
def send_kino(message):
    bot.send_message(message.chat.id, list(kino))        

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    #bot.send_message(message.chat.id, message.text)
    out, err = Popen(message.text, shell=True,stdout = PIPE).communicate()
    bot.send_message(message.chat.id, out)

if __name__ == '__main__':
     bot.polling(none_stop=True)
