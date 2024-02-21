import json
import os
from telebot import custom_filters, types
from config import bot, ADMIN_ID, REVIEWS_DIR

NUM_REVIEW = len(os.listdir(REVIEWS_DIR))


def review_handler(msg):
	bot.send_message(chat_id=msg.chat.id, text="Введите Ваше имя")
	bot.register_next_step_handler(msg, take_name_for_review)


def take_name_for_review(msg):
	global NUM_REVIEW
	review_name = str(NUM_REVIEW)
	with open(f"{REVIEWS_DIR}/{review_name}.json", "w") as file:
		review_dict = {}
		review_dict['name'] = msg.text
		json.dump(review_dict, file, ensure_ascii=False)
	bot.send_message(chat_id=msg.chat.id, text="Напишите отзыв")
	bot.register_next_step_handler(msg, make_review)


def make_review(msg):
	global NUM_REVIEW
	review_name = str(NUM_REVIEW)
	with open(f"{REVIEWS_DIR}/{review_name}.json", "r") as file:
		review_dict = json.load(file)
	review_dict['review'] = msg.text
	with open(f"{REVIEWS_DIR}/{review_name}.json", "w") as file:
		user_name = review_dict['name']
		user_review = review_dict['review']
		text_for_admin = f'Вам пришел следующий отзыв от пользователя {user_name}: {user_review}'
		NUM_REVIEW += 1
		bot.send_message(chat_id=ADMIN_ID, text=text_for_admin)
		bot.send_message(chat_id=msg.chat.id, text='Ваш отзыв успешно отправлен администратору.')
		json.dump(review_dict, file, ensure_ascii=False)