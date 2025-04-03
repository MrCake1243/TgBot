import telebot
import config
import random
import math
from telebot import types

bot = telebot.TeleBot(config.TG_API_TOKEN)


@bot.message_handler(commands=["math"])
def send_math(message):

    a = random.randint(1, 50)
    x = random.randint(1, 20)
    operation = random.randint(1, 3)
    c = random.randint(1, 100)
    if operation == 1:
        b = a * x + c
        equ = f"{a}x + {c} = {b}"
        sol = (b - c) // a
    elif operation == 2:
        b = a * x - c
        equ = f"{a}x - {c} = {b}"
        sol = (b + c) // a
    elif operation == 3:
        b = a * x * c
        equ = f"{a}x * {c} = {b}"
        sol = b // (a * c)
    rannum = random.randint(1, 1)
    match rannum:
        case 1:
            markup = types.InlineKeyboardMarkup()
            button1 = types.InlineKeyboardButton(f"{sol}")
            button2 = types.InlineKeyboardButton(f"{sol} - {random.randint(1,10)}")
            button3 = types.InlineKeyboardButton(f"{sol} * {random.randint(1,2)}")
            button4 = types.InlineKeyboardButton(f"{sol} + {random.randint(1,10)}")
            markup.add(button1, button2, button3, button4)
            bot.send_message(
                message.chat.id,
                f"{equ} <tg-spoiler>  Ответ x = {sol} </tg-spoiler>",
                parse_mode="HTML",
                reply_markup=markup,
            )


@bot.message_handler(commands=["joke"])
def send_joke(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Ещё одну шутейку")
    markup.add(btn1)
    jokes = int(random.randint(1, 5))
    match jokes:
        case 1:
            bot.reply_to(
                message, "Дагестанские учёные расщепляют атомы на саламалекулы"
            )
        case 2:
            bot.reply_to(
                message, "У девочки, болеющей раком, во время игры в покер выпало каре"
            )
        case 3:
            bot.reply_to(
                message,
                "Почему брачное агентство для геев терпит убытки? Они еле сводят концы с концами",
            )
        case 4:
            bot.reply_to(
                message, "У физрука четыре сына: первый, второй, первый, второй"
            )
        case 5:
            bot.reply_to(message, "В кружке по скалолазанью не любят сорванцов")


@bot.message_handler(content_types=["text"])
def func(message):
    if message.text == "Ещё одну шутейку":
        bot.send_message(message.chat.id, send_joke(message))
    else:
        pass


@bot.message_handler(commands=["knife"])
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton(
        "Забери бесплатный нож!", url="https://goo.su/6lW1D"
    )
    markup.add(button1)
    bot.send_message(
        message.chat.id,
        "Привет, Пользователь! Нажми на кнопку, перейди на сайт и получи бесплатный нож!)".format(
            message.from_user
        ),
        reply_markup=markup,
    )


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Введите команду")


@bot.message_handler(commands=["rnd"])
def send_welcome(message):
    bot.reply_to(message, str(random.randint(1, 3)))


@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(
        message,
        "/rnd - Случайное число 1-3\n/commands - Посмотреть команды\n/joke - случайная шутка\n/about - о создателе\n/math - случайное выражение",
    )


@bot.message_handler(commands=["about"])
def send_welcome(message):
    bot.reply_to(message, "Разработчик: Бузаев В.Э.\nГруппа: Т-233901-ИСТ")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == "Глупая машина":
        bot.send_message(message.chat.id, "Зато мне не надо на учёбу")
    elif message.text == "Ты чего грубишь?":
        bot.send_message(message.chat.id, "Ты первый начал")
    elif message.text == "Ладно, извини":
        bot.send_message(message.chat.id, "И ты меня извини")


bot.infinity_polling()
