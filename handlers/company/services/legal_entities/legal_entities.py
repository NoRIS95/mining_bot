from telebot import custom_filters, types
from config import bot

def legal_entities_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут информация для юридических лиц')