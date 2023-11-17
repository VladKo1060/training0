from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Dispatcher, CallbackContext, Filters, CommandHandler, CallbackQueryHandler, ConversationHandler
import logging
from key import TOKEN

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

WAIT_NAME, WAIT_SURNAME, WAIT_BIRTHDAY = range(3)


def ask_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_name')
    update.message.reply_text(f'Назови своё имя')

    return WAIT_NAME


def get_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_name')
    update.message.reply_text(f'Получил твоё имя')

    return ask_surname(update, context)


def ask_surname(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_surname')
    update.message.reply_text(f'Назови свою фамилию')

    return WAIT_SURNAME


def get_surname(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_surname')
    update.message.reply_text(f'Получил твою фамилию')

    return ask_birthday(update, context)


def ask_birthday(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_birthday')
    update.message.reply_text(f'Назови свой день рождения')

    return WAIT_BIRTHDAY


def get_birthday(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_birthday')
    update.message.reply_text(f'Получил твой день рождения')

    return register(update, context)


def register(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию register')
    update.message.reply_text(f'Зарегестрировал тебя')

    return ConversationHandler.END



conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('register', ask_name)],
    states={WAIT_NAME: [MessageHandler(Filters.text, get_name)],
            WAIT_SURNAME: [MessageHandler(Filters.text, get_surname)],
            WAIT_BIRTHDAY: [MessageHandler(Filters.text, get_birthday)]
            },
    fallbacks=[]
)

if __name__ == '__main__':
    updater = Updater(token=TOKEN)
    dispatcher: Dispatcher = updater.dispatcher
    dispatcher.add_handler(conversation_handler)
    updater.start_polling()
    updater.idle()
