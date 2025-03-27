import telebot
import config
import random
import math

bot = telebot.TeleBot(config.TG_API_TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Введите команду")


@bot.message_handler(commands=["rnd"])
def send_welcome(message):
    bot.reply_to(message, str(random.randint(1, 3)))


@bot.message_handler(commands=["math"])
def send_welcome(message):
    mathex = int(random.randint(1, 3))
    match mathex:
        case 1:
            a = random.randint(1, 9)
            b = random.randint(1, 9)
            c = int(a + b)
            bot.send_message(
                message.chat.id,
                f"x - {a} = {b} | x = ||{str(c)}||",
                parse_mode="MarkdownV2",
            )
        case 2:
            a = random.randint(1, 5)
            b = random.randint(1, 10)
            c = int(b - a)
            bot.send_message(
                message.chat.id,
                f"x + {a} = {b} | x = ||{str(c)}||",
                parse_mode="MarkdownV2",
            )
        case 3:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            c = int(b * a)
            bot.send_message(
                message.chat.id,
                f"x * {a} = {c} | x = ||{str(b)}||",
                parse_mode="MarkdownV2",
            )


# @bot.message_handler(commands=["discr"])
# def send_welcome(message):
#     bot.reply_to(message, "Введи a, b, c: ")
#     bot.
#     a = message.text
#     a = a.split("")
#     D = int(a[1]) * int(a[1]) - 4 * int(a[0]) * int(a[2])
#     if D >= 0:
#         bot.send_message(
#             message,
#             f"Корни уравнения: x1 = {(-int(a[1]) - int(D, 0.5))/2*int(a[0])} x1 = {(-int(a[1]) + int(D, 0.5))/2*int(a[0])}",
#         )
@bot.message_handler(commands=["joke"])
def send_welcome(message):
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


@bot.message_handler(commands=["help"])
def send_welcome(message):
    bot.reply_to(message, "rnd - Случайное число 1-3\ncommands - Посмотреть команды")


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
