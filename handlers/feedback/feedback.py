from telebot import custom_filters, types
from .review.review import review_handler
from .suggestions.suggestions import suggestions_handler
from .mistakes.mistakes import mistakes_handler

from config import bot, ADMIN_ID

def feedback_handler(msg):
	item_review = types.KeyboardButton('Ваш отзыв о компании')
	item_suggestions = types.KeyboardButton('Предложения по работе бота')
	item_mistakes = types.KeyboardButton('Нашли ошибку? Сообщите нам!')
	markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
	markup_reply.add(item_review, item_suggestions, item_mistakes)
	msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок', \
			reply_markup=markup_reply)
	bot.register_next_step_handler(msg, feedback_answer_handler)

def feedback_answer_handler(msg):
	if msg.text == 'Ваш отзыв о компании':
		review_handler(msg)
	elif msg.text == 'Предложения по работе бота':
		suggestions_handler(msg)
	elif msg.text == 'Нашли ошибку? Сообщите нам!':
		mistakes_handler(msg)