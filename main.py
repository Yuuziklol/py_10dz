from telegram import Bot
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, ConversationHandler

bot = Bot(token='5840368801:AAF_Mj2uTITlBTMDXbhHSaf1XmNPYaKU50A')
updater = Updater(token='5840368801:AAF_Mj2uTITlBTMDXbhHSaf1XmNPYaKU50A')
dispahather = updater.dispatcher

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет,\nвведи выражение ")

def input(update, context):
    text = update.message.text
    user = update.effective_chat.id
    log(user)
    log(text)
    data = parse(text)
    expression = calculate(data)
    context.bot.send_message(update.effective_chat.id,expression)
    log(expression)

def log(data):
    with open('logger.txt','a',encoding='utf=8') as file:
        file.write(str(data) + '\n')

def parse(s):
    result = []
    digit = ""
    for symbol in s:
        if symbol.isdigit():
            digit += symbol
        else:
            result.append(float(digit))
            digit = ""
            result.append(symbol)
    else:
        if digit:
            result.append(float(digit))
    return result

def calculate(lst):   
    result = 0.0
    for s in lst:
        if s == '*' or s == '/':
            if s == '*':
                index = lst.index(s)
                result = lst[index - 1] * lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] / lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    for s in lst:
        if s == '+' or s == '-':
            if s == '+':
                index = lst.index(s)
                result = lst[index - 1] + lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
            else:
                index = lst.index(s)
                result = lst[index - 1] - lst[index + 1]
                lst = lst[:index - 1] + [result] + lst[index + 2:]
    return result

start_handler = CommandHandler("start", start)
message_handler = MessageHandler(Filters.text, input)

dispahather.add_handler(start_handler)
dispahather.add_handler(message_handler)

updater.start_polling()
updater.idle()