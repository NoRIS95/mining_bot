from telebot import custom_filters, types
from config import bot

def leasing_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут информация о лизинге')