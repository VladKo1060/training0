from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import Updater, MessageHandler, Dispatcher, CallbackContext, Filters, CommandHandler, \
    ConversationHandler, CallbackQueryHandler
import logging
from key import TOKEN
from class_human import Human
from db import Data_Base

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

WHIT_DELITE_SAVE, WAIT_NAME, WAIT_SURNAME, WAIT_MIDDLE_NAME, WAIT_PHONE_NUMBER, WAIT_BIRTHDAY = range(6)

# user = Human()
db = Data_Base('Bot_Date_Base')


def scan(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id          # user_id = update.effective_chat.id

    user_in_db = db.find_user_by_id(user_id, id_str=True)

    if user_in_db is not None:
        text = '\n'.join(user_in_db.values())

        text_message = f'<b><u>Ты был найден в базе данных</u></b>\n{text}'

        buttons = [[InlineKeyboardButton(text='Отмена', callback_data='Отмена'),
                   InlineKeyboardButton(text='Перезапись', callback_data='Перезапись')]]

        keyboard = InlineKeyboardMarkup(buttons)

        context.bot.send_message(user_id, f'{text_message}', reply_markup=keyboard, parse_mode=ParseMode.HTML)
        logging.info(f'{user_id=}, функция scan. Пользователь был найден в БД')
        return WHIT_DELITE_SAVE
    else:
        logging.info(f'{user_id=}, функция scan. Пользователь не был найден в БД')
        return ask_name(update, context)


def delete_save(update: Update, context: CallbackContext):
    queuy = update.callback_query
    user_id = update.effective_chat.id

    if queuy.data in 'Перезапись':
        context.bot.send_message(user_id, f'Перезапись')
        logging.info(f'{user_id=}, функция scan. Перезапись')
        return ask_name(update, context)
    elif queuy.data in 'Отмена':
        context.bot.send_message(user_id, f'Отмена')
        logging.info(f'{user_id=}, функция scan. Отмена')
        return ConversationHandler.END


def ask_name(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id                 # update.message.from_user.id
    user_name = update.effective_user.first_name       # update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию ask_name')
    context.bot.send_message(user_id, f'Назови своё имя')       # update.message.reply_text(f'Назови своё имя')

    return WAIT_NAME


def get_name(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    context.user_data['name'] = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_name')
    update.message.reply_text(f'Получил твоё имя')

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
    context.user_data['middle_name'] = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_middle_name')
    update.message.reply_text(f'Получил твоё отчество')

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
    context.user_data['surname'] = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_surname')
    update.message.reply_text(f'Получил твою фамилию')

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
    context.user_data['phone_number'] = update.message.text
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
    context.user_data['birthday'] = update.message.text
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию get_birthday')
    update.message.reply_text(f'Получил твой день рождения')

    return register(update, context)


def register(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    logging.info(f'{user_id=}, {user_name=},  вызвал функцию register')
    # context.user_data['name'] = update.message.text
    db.write(user_id,
             context.user_data['surname'],
             context.user_data['name'],
             context.user_data['middle_name'],
             context.user_data['phone_number'],
             context.user_data['birthday'])
    text = '\n'.join(db.find_user_by_id(user_id, id_str=True).values())
    update.message.reply_text(f'Зарегестрировал тебя с данными:\n{text}')
    # user.data_print()

    return ConversationHandler.END


conversation_handler = ConversationHandler(
    entry_points=[CommandHandler('register', scan)],
    states={WHIT_DELITE_SAVE: [CallbackQueryHandler(delete_save)],
            WAIT_NAME: [MessageHandler(Filters.text, get_name)],
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
