from telebot import custom_filters, types
from config import bot

def payment_and_delivery_handler(msg):
	msg = bot.send_message(msg.chat.id, 'Тут информация об оплате и доставке')