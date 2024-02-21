from telebot import custom_filters, types
from config import bot

def info_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут текст о компании')

def soc_network_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут инфа о соцсетях')

def reviews_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут отзывы')

def requisites_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут реквизиты')