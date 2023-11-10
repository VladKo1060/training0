from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Dispatcher, CallbackContext, Filters, CommandHandler, CallbackQueryHandler, ConversationHandler
import logging
from key import TOKEN

logger = logging.getLogger(__name__)

WAIT_NAME, WAIT_SURNAME, WAIT_BIRTHDAY = range(3)


def ask_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_name')

    return WAIT_NAME


def get_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_name')

    return ask_surname(update, context)


def ask_surname(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_surname')

    return WAIT_SURNAME


def get_surname(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_surname')

    return ask_birthday(update, context)


def ask_birthday(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_birthday')

    return WAIT_BIRTHDAY


def get_birthday(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_birthday')

    return register(update, context)


def register(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию register')

    return ConversationHandler.END
