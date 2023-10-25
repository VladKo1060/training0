from telegram import Update, ReplyKeyboardMarkup, ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Dispatcher, CallbackContext, Filters, CommandHandler, CallbackQueryHandler
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
    keyboard_inline_handler = CommandHandler(['k_i', 'keyboard_inline'], do_keyboard_inline)
    callback_handler = CallbackQueryHandler(keyboard_react)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(keyboard_handler)
    dispatcher.add_handler(keyboard_inline_handler)
    dispatcher.add_handler(callback_handler)
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
    text = f'<b><u>Привет ёмаё!</u></b>\n' \
           '<i><b>Команды:</b></i>\n' \
           '<i>/start - старт, помощь\n' \
           '/k, /keyboard - клавиатура\n' \
           '/k_i, /keyboard_inline - инлаин клавиатура</i>\n\n' \
           '<a href="https://github.com/VladKo1060/training0/blob/main/pyTelebot.py">Git бота</a>'

    update.message.reply_text(f'{user_id=}\n{user_name=}')
    update.message.reply_text(f'{text}', parse_mode=ParseMode.HTML)
    logging.info(f'{user_id=}, {user_name=}, {text}')


def do_keyboard(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    buttons = [
        ['1', '2', '3', '4'],
        ['/start', '/keyboard']
    ]
    keyboard = ReplyKeyboardMarkup(buttons)

    update.message.reply_text(f'{user_id=}\nКлава к вашим услугам', reply_markup=keyboard)
    logging.info(f'{user_id=}, функция клавы')


def do_keyboard_inline(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    # buttons = [
    #     [InlineKeyboardButton(text='1', callback_data=''), InlineKeyboardButton(text='2', callback_data=''), InlineKeyboardButton(text='Разраб', callback_data='')],
    #     [InlineKeyboardButton(text='/start', callback_data=''), InlineKeyboardButton(text='/keyboard', callback_data='')]
    # ]

    buttons = [
        ['1', '2', '3', '4'],
        ['/start', '/keyboard']
    ]

    inline_buttons = [[InlineKeyboardButton(text=text, callback_data=text) for text in row] for row in buttons]

    keyboard = InlineKeyboardMarkup(inline_buttons)

    update.message.reply_text(f'{user_id=}\nИнлаин клава к вашим услугам', reply_markup=keyboard)
    logging.info(f'{user_id=}, функция инлаин клавы')


def keyboard_react(update: Update, context: CallbackContext):
    queuy = update.callback_query
    user_id = update.effective_user.id

    buttons = [
        ['1', '2', '3', '4'],
        ['/start', '/keyboard']
    ]
    for row in buttons:
        if queuy.data in row:
            row.pop(row.index(queuy.data))

    inline_buttons = [[InlineKeyboardButton(text=text, callback_data=text) for text in row] for row in buttons]

    keyboard = InlineKeyboardMarkup(inline_buttons)
    queuy.edit_message_reply_markup(keyboard)  # (f'{user_id=}\nТхы што вхыврал?')
    logging.info(f'{user_id=}, функция радакции инлаин клавы')


if __name__ == '__main__':
    main()
