from telebot import custom_filters, types
from config import bot

def warranty_svc_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут информация о гарантийном обслуживании')