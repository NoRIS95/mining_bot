from telebot import custom_filters, types
from .mining_hotel.mining_hotel import *
from .custom_equipment.custom_equipment import *
from .available_equipment.available_equipment import *
from .payment_and_delivery.payment_and_delivery import *
from .leasing.leasing import *
from .legal_entities.legal_entities import *
from .installment_plan.installment_plan import *
from config import bot

def services_handler(msg):
	item_mining_hotel = types.KeyboardButton('Майнинг отель')
	item_warranty_svc = types.KeyboardButton('Гарантийное обслуживание')
	item_custom_equipment = types.KeyboardButton('Оборудование под заказ')
	item_available_equipment = types.KeyboardButton('Оборудование из наличия')
	item_payment_and_delivery = types.KeyboardButton('Оплата и доставка')
	item_leasing = types.KeyboardButton('Лизинг')
	item_legal_entities = types.KeyboardButton('Для юридических лиц')
	item_installment_plan = types.KeyboardButton('Рассрочка')
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup_reply.add(item_mining_hotel, item_warranty_svc, \
	 item_custom_equipment, item_available_equipment, \
	 item_payment_and_delivery, item_leasing, \
	 item_legal_entities, item_installment_plan)
	msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок', \
			reply_markup=markup_reply)
	bot.register_next_step_handler(msg, services_answer_handler)

def services_answer_handler(msg):
	if msg.text == 'Майнинг отель':
		mining_hotel_handler(msg)
	elif msg.text == 'Гарантийное обслуживание':
		warranty_svc_handler(msg)
	elif msg.text == 'Оборудование под заказ':
		custom_equipment_handler(msg)
	elif msg.text == 'Оборудование из наличия':
		available_equipment_handler(msg)
	elif msg.text == 'Оплата и доставка':
		payment_and_delivery_handler(msg)
	elif msg.text == 'Лизинг':
		leasing_handler(msg)
	elif msg.text == 'Для юридических лиц':
		legal_entities_handler(msg)
	elif msg.text == 'Рассрочка':
		installment_plan_handler(msg)