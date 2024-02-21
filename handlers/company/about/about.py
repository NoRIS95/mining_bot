from telebot import custom_filters, types
from .info.info import *
from config import bot

def about_handler(msg):
	item_info = types.KeyboardButton('О компании')
	item_soc_network = types.KeyboardButton('Наши соц. Сети')
	item_reviews = types.KeyboardButton('Отзывы')
	item_requisites = types.KeyboardButton('Реквизиты')
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup_reply.add(item_info, item_soc_network,\
	 item_reviews, item_requisites)
	msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок', \
			reply_markup=markup_reply)
	bot.register_next_step_handler(msg, about_answer_handler)


def about_answer_handler(msg):
	if msg.text == 'О компании':
		info_handler(msg)
	elif msg.text == 'Наши соц. Сети':
		soc_network_handler(msg)
	elif msg.text == 'Отзывы':
		reviews_handler_handler(msg)
	elif msg.text == 'Реквизиты':
		requisites_handler(msg)

