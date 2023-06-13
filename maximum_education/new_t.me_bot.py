import telebot
import requests
from bs4 import BeautifulSoup
import random

token = '5690575968:AAGbQlitvSyFQ4eYM_nkoCj2X5H_1ZXWHmk'
bott = telebot.TeleBot(token)

@bott.message_handler(commands=['start','help'])
def send_welcome(message):
    welcome_text = 'Привет я телегамм бот!'
    bott.send_message(message.chat.id, welcome_text)

@bott.message_handler(commands=['poem'])
def send_welcome(message):
    poem_text = 'ялялялялляляляляляляля всё!'
    bott.send_message(message.chat.id, poem_text)

@bott.message_handler(commands=['fact'])
def send_welcome(message):
    responce = requests.get('https://i-fakt.ru')
    responce=responce.content
    html = BeautifulSoup(responce, 'html.parser')
    fact = random.choice(html.find_all(class_='p-2 clearfix'))
    fact_linl = fact.a.attrs['href']
    bott.send_message(message.chat.id, fact_linl)
bott.polling()