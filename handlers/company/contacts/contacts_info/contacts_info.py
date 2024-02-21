from telebot import custom_filters, types
from config import bot

def contacts_Moscow_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут контактные данные филиала Москвы')

def contacts_Irkutsk_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут контактные данные филиала Москвы')

def support_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут тех.поддежка')
