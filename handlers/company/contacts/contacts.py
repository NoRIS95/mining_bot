from telebot import custom_filters, types
from .contacts_info.contacts_info import *
from config import bot

def contacts_handler(msg):
	item_Moscow = types.KeyboardButton('Москва')
	item_Irkutsk = types.KeyboardButton('Иркутск')
	item_support = types.KeyboardButton('Тех. поддержка')
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup_reply.add(item_Moscow, item_Irkutsk, item_support)
	msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок', \
			reply_markup=markup_reply)
	bot.register_next_step_handler(msg, contacts_answer_handler)


def contacts_answer_handler(msg):
	if msg.text == 'Москва':
		contacts_Moscow_handler(msg)
	elif msg.text == 'Иркутск':
		contacts_Irkutsk_handler(msg)
	elif msg.text == 'Тех. поддержка':
		support_handler(msg)
