from telegram import Update
from telegram.ext import Updater, MessageHandler, Dispatcher, CallbackContext, Filters, CommandHandler, ConversationHandler
import logging
from key import TOKEN
from class_human import Human
from db import Data_Base

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

WAIT_NAME, WAIT_SURNAME, WAIT_MIDDLE_NAME, WAIT_PHONE_NUMBER, WAIT_BIRTHDAY = range(5)

user = Human()
db = Data_Base('Bot_Date_Base')


def ask_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_name')
    update.message.reply_text(f'Назови своё имя')

    return WAIT_NAME


def get_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    user.name = update.message.text
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
    user.surname = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_surname')
    update.message.reply_text(f'Получил твою фамилию')

    return ask_middle_name(update, context)


def ask_middle_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_middle_name')
    update.message.reply_text(f'Назови своё отчество')

    return WAIT_MIDDLE_NAME


def get_middle_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    user.middle_name = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_middle_name')
    update.message.reply_text(f'Получил твоё отчество')

    return ask_phone_number(update, context)


def ask_phone_number(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_phone_number')
    update.message.reply_text(f'Назови свой номер телефона')

    return WAIT_PHONE_NUMBER


def get_phone_number(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    user.phone_number = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_phone_number')
    update.message.reply_text(f'Получил твой номер телефона')

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
    user.birthday = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_birthday')
    update.message.reply_text(f'Получил твой день рождения')

    return register(update, context)


def register(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию register')
    db.write_to_date_base(user_id, user.surname, user.name, user.middle_name, user.phone_number, user.birthday)
    update.message.reply_text(f'Зарегестрировал тебя')
    # user.data_print()

    return ConversationHandler.END


conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('register', ask_name)],
    states={WAIT_NAME: [MessageHandler(Filters.text, get_name)],
            WAIT_SURNAME: [MessageHandler(Filters.text, get_surname)],
            WAIT_MIDDLE_NAME: [MessageHandler(Filters.text, get_middle_name)],
            WAIT_PHONE_NUMBER: [MessageHandler(Filters.text, get_phone_number)],
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
