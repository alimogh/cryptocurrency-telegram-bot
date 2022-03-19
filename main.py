import requests
import telebot
import config
from config import API_TOKEN
from telebot import types
from datetime import datetime

bot = telebot.TeleBot(API_TOKEN) # Токен вставляем в config.py

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kb.add('Узнать курс')
    kb.add('FAQ')
    bot.send_message(message.chat.id, 'Приветствую!\n\nС помощью этого бота вы можете узнавать актуальный курс криптовалют.', reply_markup=kb, parse_mode='Markdown')

@bot.message_handler(content_types=['text'])
def first(message):

    menu = types.ReplyKeyboardMarkup(resize_keyboard=True) # Создаем клавиатуру
    # Добавляем кнопки
    menu.add('Узнать курс') 
    menu.add('FAQ')
    # Создаем еще одну клавиатуру
    kb2 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # Создаем кнопки для второй клавиатуры
    kb2.add('Bitcoin')
    kb2.add('Etherium')
    kb2.add('Litecoin')
    kb2.add('Dogecoin')
    kb2.add('Dash')
    kb2.add('⬅️ Назад')

    if message.text == 'Узнать курс':
        bot.send_message(message.chat.id, '*Выберите нужную криптовалюту:*', reply_markup=kb2, parse_mode='Markdown')

    if message.text == 'Bitcoin':
        req = requests.get('https://yobit.net/api/3/ticker/btc_usdt') # Запрашиваем BTC-USD курс через API Yobit
        req_rub = requests.get('https://yobit.net/api/3/ticker/btc_rur') # Запрашиваем BTC-RUB курс через API Yobit
        response = req.json()
        response_rub = req_rub.json()
        send_price = response["btc_usdt"]["sell"]
        send_price_rub = response_rub["btc_rur"]["sell"]

        bot.send_message(message.chat.id, f"*Bitcoin*\n\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\n\nBTC-USD: *{send_price}$*\nBTC-RUB: *{send_price_rub} RUB*", parse_mode='Markdown')   

    if message.text == 'Etherium':
        req = requests.get('https://yobit.net/api/3/ticker/eth_usdt') # Запрашиваем ETH-USD курс через API Yobit
        req_rub = requests.get('https://yobit.net/api/3/ticker/eth_rur') # Запрашиваем ETH-RUB курс через API Yobit
        response = req.json()
        response_rub = req_rub.json()
        send_price = response["eth_usdt"]["sell"]
        send_price_rub = response_rub["eth_rur"]["sell"]

        bot.send_message(message.chat.id, f"*Etherium*\n\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\n\nETH-USD: *{send_price}$*\nETH-RUB: *{send_price_rub} RUB*", parse_mode='Markdown')   

    if message.text == 'Litecoin':
        req = requests.get('https://yobit.net/api/3/ticker/ltc_usdt') # Запрашиваем LTC-USD курс через API Yobit
        req_rub = requests.get('https://yobit.net/api/3/ticker/ltc_rur') # Запрашиваем LTC-RUB курс через API Yobit
        response = req.json()
        response_rub = req_rub.json()
        send_price = response["ltc_usdt"]["sell"]
        send_price_rub = response_rub["ltc_rur"]["sell"]

        bot.send_message(message.chat.id, f"*Litecoin*\n\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\n\nLTC-RUB: *{send_price}$*\nLTC-RUB: *{send_price_rub} RUB*", parse_mode='Markdown')

    if message.text == 'Dogecoin':
        req = requests.get('https://yobit.net/api/3/ticker/doge_usdt') # Запрашиваем DOGE-USD курс через API Yobit
        req_rub = requests.get('https://yobit.net/api/3/ticker/doge_rur') # Запрашиваем DOGE-RUB курс через API Yobit
        response = req.json()
        response_rub = req_rub.json()
        send_price = response["doge_usdt"]["sell"]
        send_price_rub = response_rub["doge_rur"]["sell"]

        bot.send_message(message.chat.id, f"*Dogecoin*\n\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\n\nDOGE-USD: *{send_price}$*\nDOGE-RUB: *{send_price_rub} RUB*", parse_mode='Markdown')

    if message.text == 'Dash':
        req = requests.get('https://yobit.net/api/3/ticker/dash_usd') # Запрашиваем DASH-USD курс через API Yobit
        req_rub = requests.get('https://yobit.net/api/3/ticker/dash_rur') # Запрашиваем DASH-RUB курс через API Yobit
        response = req.json()
        response_rub = req_rub.json()
        send_price = response["dash_usd"]["sell"]
        send_price_rub = response_rub["dash_rur"]["sell"]

        bot.send_message(message.chat.id, f"*DASH*\n\n{datetime.now().strftime('%d-%m-%Y %H:%M')}\n\nDOGE-USD: *{send_price}$*\nDOGE-RUB: *{send_price_rub} RUB*", parse_mode='Markdown')          

    if message.text == '⬅️ Назад':
        bot.send_message(message.chat.id, '*Вы вернулись в главное меню*', reply_markup=menu, parse_mode='Markdown')

    if message.text == 'FAQ':
        bot.send_message(message.chat.id, 'Бот, который берет актуальную информацию с сайта Yobit.net', reply_markup=menu, parse_mode='Markdown')

    else:
        bot.send_message(message.chat.id, 'Неверная команда!')

bot.infinity_polling()