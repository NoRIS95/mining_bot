from telebot import custom_filters, types
from config import bot

def available_equipment_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут информация об оборудовании из наличия')
