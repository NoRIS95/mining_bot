from telebot import custom_filters, types
from .about.about import about_handler
from .contacts.contacts import contacts_handler
from .services.services import services_handler

from config import bot

def company_handler(msg):
	item_about = types.KeyboardButton('О нас')
	item_services = types.KeyboardButton('Услуги')
	item_contacts = types.KeyboardButton('Контакты')
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup_reply.add(item_about, item_services, item_contacts)
	msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок', \
			reply_markup=markup_reply)
	bot.register_next_step_handler(msg, company_answer_handler)

def company_answer_handler(msg):
	if msg.text == 'О нас':
		about_handler(msg)
	elif msg.text == 'Услуги':
		services_handler(msg)
	elif msg.text == 'Контакты':
		contacts_handler(msg)