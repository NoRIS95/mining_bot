import json
import os
from telebot import custom_filters, types
from config import bot, ADMIN_ID, APPLICATIONS_DIR

NUM_APPLICATION = len(os.listdir(APPLICATIONS_DIR))

def leaving_request_handler(msg):
	bot.send_message(chat_id=msg.chat.id, text="Введите Ваши фамилию, имя и отчество")
	bot.register_next_step_handler(msg, take_fullname_for_application)


def take_fullname_for_application(msg):
	global NUM_APPLICATION
	application_id = str(NUM_APPLICATION)
	with open(f"{APPLICATIONS_DIR}/{application_id}.json", "w") as file:
		application_dict = {}
		application_dict['fullname'] = msg.text
		json.dump(application_dict, file, ensure_ascii=False)
	bot.send_message(chat_id=msg.chat.id, text="Введите город:")
	bot.register_next_step_handler(msg, take_city_for_application)


def take_city_for_application(msg):
	global NUM_APPLICATION
	application_id = str(NUM_APPLICATION)
	with open(f"{APPLICATIONS_DIR}/{application_id}.json", "r") as file:
		application_dict = json.load(file)
	application_dict['city'] = msg.text
	with open(f"{APPLICATIONS_DIR}/{application_id}.json", "w") as file:
		json.dump(application_dict, file, ensure_ascii=False)
	bot.send_message(chat_id=msg.chat.id, text="Введите Ваш контактный телефон:")
	bot.register_next_step_handler(msg, take_phone_for_application)

def take_phone_for_application(msg):
	global NUM_APPLICATION
	application_id = str(NUM_APPLICATION)
	with open(f"{APPLICATIONS_DIR}/{application_id}.json", "r") as file:
		application_dict = json.load(file)
	application_dict['phone'] = msg.text
	with open(f"{APPLICATIONS_DIR}/{application_id}.json", "w") as file:
		json.dump(application_dict, file, ensure_ascii=False)
	bot.send_message(chat_id=msg.chat.id, text="Введите Ваш e-mail:")
	bot.register_next_step_handler(msg, make_new_application)

def make_new_application(msg):
	global NUM_APPLICATION
	application_id = str(NUM_APPLICATION)
	with open(f"{APPLICATIONS_DIR}/{application_id}.json", "r") as file:
		application_dict = json.load(file)
	application_dict['e-mail'] = msg.text
	with open(f"{APPLICATIONS_DIR}/{application_id}.json", "w") as file:
		client_fullname = application_dict['fullname']
		client_city = application_dict['city']
		client_phone= application_dict['phone']
		client_e_mail = application_dict['e-mail']
		text_for_admin = f'Вам пришла новая заявка на майнинг-отель:\
		 \n ФИО клиента: {client_fullname} \
		 \n Город: {client_city} \
		 \n Телефон: {client_phone} \
		 \n E-mail: {client_e_mail}'
		NUM_APPLICATION += 1
		bot.send_message(chat_id=ADMIN_ID, text=text_for_admin)
		bot.send_message(chat_id=msg.chat.id, text='Ваша заявка успешно отправлена администратору. С Вами скоро свяжутся.')
		json.dump(application_dict, file, ensure_ascii=False)

