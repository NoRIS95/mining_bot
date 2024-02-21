import json
import os
from telebot import custom_filters, types
from config import bot, ADMIN_ID, SUGGESTIONS_DIR
import telebot


NUM_SUGGESTIONS = len(os.listdir(SUGGESTIONS_DIR))

def suggestions_handler(msg):
	bot.send_message(chat_id=msg.chat.id, text="Введите Ваше имя")
	bot.register_next_step_handler(msg, take_name_for_suggestion)

def take_name_for_suggestion(msg):
	global NUM_SUGGESTIONS
	suggestion_id = str(NUM_SUGGESTIONS)
	with open(f"{SUGGESTIONS_DIR}/{suggestion_id}.json", "w") as file:
		suggestion_dict = {}
		suggestion_dict['name'] = msg.text
		json.dump(suggestion_dict, file, ensure_ascii=False)
	bot.send_message(chat_id=msg.chat.id, text="Напишите Ваше пожелание")
	bot.register_next_step_handler(msg, make_suggestion)


def make_suggestion(msg):
	global NUM_SUGGESTIONS
	suggestion_id = str(NUM_SUGGESTIONS)
	with open(f"{SUGGESTIONS_DIR}/{suggestion_id}.json", "r") as file:
		suggestion_dict = json.load(file)
	suggestion_dict['suggestion'] = msg.text
	with open(f"{SUGGESTIONS_DIR}/{suggestion_id}.json", "w") as file:
		user_name = suggestion_dict['name']
		user_suggestion = suggestion_dict['suggestion']
		text_for_admin = f'Вам пришло следующее пожелание по работе бота от пользователя {user_name}: {user_suggestion}'
		NUM_SUGGESTIONS += 1
		bot.send_message(chat_id=ADMIN_ID, text=text_for_admin)
		bot.send_message(chat_id=msg.chat.id, text='Ваше пожелание по работе бота успешно отправлено администратору.')
		json.dump(suggestion_dict, file, ensure_ascii=False)