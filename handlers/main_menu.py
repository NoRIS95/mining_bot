from config import bot
from handlers.company.company import company_handler
from handlers.feedback.feedback import feedback_handler
from telebot import types

@bot.message_handler(commands=["start"])
def hello_message(message):
    # user_id = str(message.from_user.id)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}! Введите /info')
    # USER_CONDITIONS.data[user_id] = StatusDialog.STATUS_OF_ASK_CITY.value

@bot.message_handler(commands=['info'])
def get_user_info(message):
	markup_reply = types.ReplyKeyboardMarkup()
	item_yes = types.KeyboardButton(text= 'ДА')
	item_no = types.KeyboardButton(text = 'НЕТ')

	markup_reply.add(item_yes, item_no)
	msg = bot.send_message(message.chat.id, 'Желаете узнать небольшую информацию о нас', reply_markup = markup_reply)
	bot.register_next_step_handler(msg, main_menu)

# @bot.callback_query_handler(func = lambda call: True)
def main_menu(msg):
	if msg.text == 'ДА':
		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_support = types.KeyboardButton('Тех.поддержка')
		item_crypto_rates = types.KeyboardButton('Курсы криптовалют')
		item_calc_mining = types.KeyboardButton('Калькулятор майнинга')
		item_company = types.KeyboardButton('Компания')
		item_feedback = types.KeyboardButton('Обратная связь')
		item_catalog = types.KeyboardButton('Каталог')
		item_education = types.KeyboardButton('Обучение')
		markup_reply.add(item_support, item_crypto_rates, item_calc_mining, item_company, \
			item_feedback, item_catalog, item_education)
		msg = bot.send_message(msg.chat.id, 'Нажмите на одну из кнопок', \
			reply_markup=markup_reply)
		bot.register_next_step_handler(msg, main_menu_answer_handler) # https://github.com/eternnoir/pyTelegramBotAPI/blob/master/examples/step_example.py
	elif msg.text == 'НЕТ':
		pass

def main_menu_answer_handler(msg):
	# обработчик ответа
	if msg.text == 'Компания':
		company_handler(msg)
	elif msg.text == 'Тех.поддержка':
		# bot.register_next_step_handler(msg, support_handler)
		pass
	elif msg.text == 'Обратная связь':
		feedback_handler(msg)