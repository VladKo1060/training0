from datetime import datetime
from telegram import Update, ReplyKeyboardMarkup, ParseMode
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Dispatcher, CallbackContext, Filters, CommandHandler, CallbackQueryHandler
from FSM import conversation_handler
import logging
from key import TOKEN

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    updater = Updater(token=TOKEN)
    dispatcher: Dispatcher = updater.dispatcher

    echo_handler = MessageHandler(Filters.text, do_echo)
    start_handler = CommandHandler(['start', 'help'], do_keyboard_inline)
    keyboard_handler = CommandHandler(['k', 'keyboard'], do_keyboard)
    # keyboard_inline_handler = CommandHandler(['k_i', 'keyboard_inline'], do_keyboard_inline)
    set_timer_handler = MessageHandler(Filters.text('Старт'), set_timer)
    stop_timer_handler = MessageHandler(Filters.text('Стоп'), stop_timer)
    callback_handler = CallbackQueryHandler(keyboard_react)

    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(conversation_handler)
    dispatcher.add_handler(keyboard_handler)
    # dispatcher.add_handler(keyboard_inline_handler)
    dispatcher.add_handler(callback_handler)
    dispatcher.add_handler(set_timer_handler)
    dispatcher.add_handler(stop_timer_handler)
    dispatcher.add_handler(echo_handler)

    updater.start_polling()
    updater.idle()


def do_echo(update: Update, context: CallbackContext):
    user_id = update.message.from_user.id
    user_name = update.message.from_user.name
    text = update.message.text

    update.message.reply_text(f'{user_id=}\n{user_name=}\n{text}')
    logging.info(f'{user_id=}, {user_name=}, {text}')


# def do_start(update: Update, context: CallbackContext):
#     user_id = update.message.from_user.id
#     user_name = update.message.from_user.name
#     text = f'<b><u>Привет ёмаё!</u></b>\n' \
#            '<i><b>Команды:</b></i>\n' \
#            '<i>/start - старт, помощь\n' \
#            '/k, /keyboard - клавиатура\n' \
#            '/k_i, /keyboard_inline - инлаин клавиатура\n' \
#            '/timer</i>\n\n' \
#            '<a href="https://github.com/VladKo1060/training0/blob/main/pyTelebot.py">Git бота</a>'
#
#     update.message.reply_text(f'{user_id=}\n{user_name=}')
#     update.message.reply_text(f'{text}', parse_mode=ParseMode.HTML)
#     logging.info(f'{user_id=}, {user_name=}, {text}')


def do_keyboard(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id
    user_name = update.effective_user.name
    buttons = [
        ['Старт'],
        ['Стоп']
    ]
    keyboard = ReplyKeyboardMarkup(buttons)

    context.bot.send_message(user_id, f'Панель управления таймером к вашим услугам', reply_markup=keyboard)
    logging.info(f'{user_id=}, {user_name=}  функция клавы')


def do_keyboard_inline(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id
    text_message = f'<b><u>Приветствую тебя, {update.effective_user.first_name}</u></b>'

    buttons = [
        [InlineKeyboardButton(text='Помощь', callback_data='Помощь'), InlineKeyboardButton(text='Таймер', callback_data='Таймер')],
        [InlineKeyboardButton(text='Git проекта', url="https://github.com/VladKo1060/training0/blob/main/pyTelebot.py"), InlineKeyboardButton(text='Написать разработчику', url='https://t.me/kolodezhv')]
    ]

    # inline_buttons = [[InlineKeyboardButton(text=text, callback_data=text) for text in row] for row in buttons]

    keyboard = InlineKeyboardMarkup(buttons)

    context.bot.send_message(user_id, f'{text_message}', reply_markup=keyboard, parse_mode=ParseMode.HTML)
    logging.info(f'{user_id=}, функция инлаин клавы')


def keyboard_react(update: Update, context: CallbackContext):
    queuy = update.callback_query
    user_id = update.effective_chat.id

    if queuy.data in 'Помощь':
        do_keyboard_inline(update, context)
        logging.info(f'{user_id=}, Старт')
    elif queuy.data in 'Таймер':
        do_keyboard(update, context)
        logging.info(f'{user_id=}, Таймер')
    # elif queuy.data in 'Git проекта':
    #     context.bot.send_message(
    #         user_id,
    #         f'<a href="https://github.com/VladKo1060/training0/blob/main/pyTelebot.py">Git бота</a>',
    #         parse_mode=ParseMode.HTML
    #     )
    #     logging.info(f'{user_id=}, Git проекта')
    # elif queuy.data in 'Написать разработчику':
    #     context.bot.send_message(user_id, f'Написать разработчику')

    # inline_buttons = [[InlineKeyboardButton(text=text, callback_data=text) for text in row] for row in buttons]

    # keyboard = InlineKeyboardMarkup(inline_buttons)
    # queuy.edit_message_reply_markup(keyboard)  # (f'{user_id=}\nТхы што вхыврал?')
    # logging.info(f'{user_id=}, функция радакции инлаин клавы')


def set_timer(update: Update, context: CallbackContext):
    context.bot_data['user_id'] = update.effective_chat.id
    context.bot_data['timer'] = datetime.now()
    context.bot_data['timer_job'] = context.job_queue.run_repeating(show_second, 1)


def show_second(context: CallbackContext):
    message_id = context.bot_data.get('message_id', None)
    user_id = context.bot_data['user_id']
    timer = datetime.now() - context.bot_data['timer']
    timer = timer.seconds
    text = f'прошло {timer} секунд'
    text += '\nнажмите стоп на клавиатуре чтобы остановить таймер'
    if not message_id:
        message = context.bot.send_message(user_id, text)
        context.bot_data['message_id'] = message.message_id
    else:
        context.bot.edit_message_text(text, chat_id=user_id, message_id=message_id)


def stop_timer(update: Update, context: CallbackContext):
    context.bot_data['timer_job'].schedule_removal()
    context.bot_data.clear()


if __name__ == '__main__':
    main()
