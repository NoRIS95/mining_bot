from telebot import custom_filters, types
from .information_hotel.information_hotel import *
from .hotel_leaving_request.hotel_leaving_request import *
from config import bot

def mining_hotel_handler(msg):
	item_information = types.KeyboardButton('Информация')
	item_leaving_request = types.KeyboardButton('Оставить заявку')
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup_reply.add(item_information, item_leaving_request)
	msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок', \
			reply_markup=markup_reply)
	bot.register_next_step_handler(msg, mining_hotel_answer_handler)

def mining_hotel_answer_handler(msg):
	if msg.text == 'Информация':
		information_handler(msg)
	elif msg.text == 'Оставить заявку':
		leaving_request_handler(msg)