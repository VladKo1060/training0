from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Dispatcher, CallbackContext, Filters, CommandHandler
import logging
from key import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    updater = Updater(token=TOKEN)
    dispatcher: Dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.text, do_echo)
    start_handler = CommandHandler('start', do_start)
    keyboard_handler = CommandHandler(['k', 'keyboard'], do_keyboard)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(keyboard_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    text = update.message.text

    update.message.reply_text(f'{user_id=}\n{user_name=}\n{text}')
    logging.info(f'{user_id=}, {user_name=}, {text}')


def do_start(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    text = 'Привет ёмаё!'

    update.message.reply_text(f'{user_id=}\n{user_name=}\n{text}')
    logging.info(f'{user_id=}, {user_name=}, {text}')


def do_keyboard(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    buttons = [
        ['1', '2', '3', '4'],
        ['2', '3', '4', '5']
    ]
    keyboard = ReplyKeyboardMarkup(buttons)

    update.message.reply_text(f'{user_id=}\nКлава к вашим услугам', reply_markup=keyboard)


if __name__ == '__main__':
    main()
