import json
import os
from telebot import custom_filters, types
from config import bot, ADMIN_ID, MISTAKES_DIR
import telebot

NUM_MISTAKES = len(os.listdir(MISTAKES_DIR))


def mistakes_handler(msg):
	bot.send_message(chat_id=msg.chat.id, text="Введите Ваше имя")
	bot.register_next_step_handler(msg,  take_name_for_mistake)

def take_name_for_mistake(msg):
	global NUM_MISTAKES
	mistake_id = str(NUM_MISTAKES)
	mistake_dir = f'./mistakes/{mistake_id}'
	if not os.path.isdir(mistake_dir):
		os.mkdir(mistake_dir)
	with open(f"{MISTAKES_DIR}/{mistake_id}/{mistake_id}.json", "w") as file:
		mistake_dict = {}
		mistake_dict['name'] = msg.text
		json.dump(mistake_dict, file, ensure_ascii=False)
	bot.send_message(chat_id=msg.chat.id, text="Опишите проблему (можно прикрепить фото),\
	 мы сообщим о ней администратору.")
	bot.register_next_step_handler(msg,  mistakes_echo)

def mistakes_echo(msg):
	global NUM_MISTAKES
	mistake_id = str(NUM_MISTAKES)
	mistake_dir = f'./mistakes/{mistake_id}'
	if msg.text:
		text_mistake = msg.text
		with open(f"{mistake_dir}/{mistake_id}.txt", "w") as file:
			file.write(text_mistake)
		with open(f"{mistake_dir}/{mistake_id}.json", "r") as file:
			mistake_dict = json.load(file)
		user_name = mistake_dict['name']
		with open(f"{mistake_dir}/{mistake_id}.json", "w") as file:
			mistake_dict = {}
			mistake_dict['name'] = user_name 
			mistake_dict['photo'] = None
			mistake_dict['text'] = text_mistake
			text_for_admin = f'Вам пришло уведомление об ошибке в работе бота \
			 от пользователя {user_name}: {text_mistake}'
			NUM_MISTAKES += 1
			bot.send_message(chat_id=ADMIN_ID, text=text_for_admin)
			bot.send_message(chat_id=msg.chat.id, text='Сообщение об ошибке отправлено администратору.')
			json.dump(mistake_dict, file, ensure_ascii=False)
	elif msg.caption:
		text_mistake = msg.caption
		photo = msg.photo[-1]
		file_info = bot.get_file(photo.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		save_path = f'{mistake_dir}/{mistake_id}.jpg'
		with open(save_path, 'wb') as new_file:
			new_file.write(downloaded_file)
		# bot.reply_to(message, 'Фотография сохранена.')
		with open(f"{mistake_dir}/{mistake_id}.txt", "w") as file:
			file.write(text_mistake)
		with open(f"{mistake_dir}/{mistake_id}.json", "r") as file:
			mistake_dict = json.load(file)
		user_name = mistake_dict['name']
		with open(f"{mistake_dir}/{mistake_id}.json", "w") as file:
			mistake_dict = {}
			mistake_dict['name'] = user_name
			mistake_dict['text'] = text_mistake
			mistake_dict['photo'] = msg.photo[0].file_id
			text_for_admin = f'Вам пришло уведомление об ошибке в работе бота \
			 от пользователя {user_name}: {text_mistake}'
			NUM_MISTAKES += 1
			bot.send_photo(ADMIN_ID, msg.photo[0].file_id, caption=text_for_admin)
			bot.send_message(chat_id=msg.chat.id, text='Сообщение об ошибке отправлено администратору.')
			json.dump(mistake_dict, file, ensure_ascii=False)
	elif all([msg.photo is not None, msg.caption is None ]):
		text_mistake = None
		photo = msg.photo[-1]
		file_info = bot.get_file(photo.file_id)
		downloaded_file = bot.download_file(file_info.file_path)
		save_path = f'{mistake_dir}/{mistake_id}.jpg'
		with open(save_path, 'wb') as new_file:
			new_file.write(downloaded_file)
		with open(f"{MISTAKES_DIR}/{mistake_id}/{mistake_id}.txt", "w") as file:
			file.write('Пользователь прислал только фото ошибки, не сопроводив это фото текстом.')
		with open(f"{mistake_dir}/{mistake_id}.json", "r") as file:
			mistake_dict = json.load(file)
		user_name = mistake_dict['name']
		with open(f"{mistake_dir}/{mistake_id}.json", "w") as file:
			mistake_dict = {}
			mistake_dict['name'] = user_name
			mistake_dict['text'] = text_mistake
			mistake_dict['photo'] = msg.photo[0].file_id
			text_for_admin = f'Вам пришло уведомление об ошибке в работе бота \
			 от пользователя {user_name} (пользователь прислал только фото ошибки)'
			NUM_MISTAKES += 1
			bot.send_photo(ADMIN_ID, msg.photo[0].file_id, caption=text_for_admin)
			bot.send_message(chat_id=msg.chat.id, text='Сообщение об ошибке отправлено администратору.')
			json.dump(mistake_dict, file, ensure_ascii=False)
	else:
		pass