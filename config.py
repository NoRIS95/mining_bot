import os
import json
from dotenv import load_dotenv, find_dotenv
import telebot # telebot


load_dotenv()
TG_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
bot = telebot.TeleBot(TG_TOKEN)
APPLICATIONS_DIR = './applications/'
if not os.path.isdir(APPLICATIONS_DIR):
    os.mkdir(APPLICATIONS_DIR)
REVIEWS_DIR = './user_reviews/'
if not os.path.isdir(REVIEWS_DIR):
    os.mkdir(REVIEWS_DIR)
MISTAKES_DIR = './mistakes/'
if not os.path.isdir(MISTAKES_DIR):
    os.mkdir(MISTAKES_DIR)
SUGGESTIONS_DIR = './suggestions/'
if not os.path.isdir(SUGGESTIONS_DIR):
    os.mkdir(SUGGESTIONS_DIR)