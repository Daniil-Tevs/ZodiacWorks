import telebot
import re

from zodiac import get_zodiac
from totem_animal import totem_animal
from number_name import calculate_name
from destiny_number import get_description
from date_birthday import get_decode_birthday
from horoscope import get_horoscope_today

token = '6232507877:AAF5qdMgv0HAQHWMgggi8Nk1PDK6DOw4zho'
bot = telebot.TeleBot(token)
user_states = {}


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     "Привет💫 \nЯ телеграмм бот <strong>ZodiacWorks</strong>. Я занимаюсь <i>тёмными делами</i> в области нимерологии и астрологии🪐",
                     parse_mode='HTML')
    help_message(message)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     "<strong>Вот список моего функционала</strong>:\n1) Число судьбы - /destiny_number\n2) День рождения в нумерологии - /day_birthday\n3) Ваш знак зодиака - /zodiac\n4) Тотемное животное - /totem_animal\n5) Нумерология по вашему имени - /value_name\n6) Гороскоп на сегодня - /horoscope",
                     parse_mode='HTML')


@bot.message_handler(commands=['destiny_number'])
def destiny_number(message):
    bot.send_message(message.chat.id, 'Введите вашу дату рождения в формате дд.мм.гггг. Например, 27.12.2003',
                     parse_mode='HTML')
    user_states[message.chat.id] = 'destiny_number'


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'destiny_number')
def get_destiny_number(message):
    match = re.search(r'\d{2}\.\d{2}\.\d{4}', message.text)
    if match:
        mes = match.group()
        number = 0
        while len(mes) != 1:
            number = 0
            for i in mes:
                if i != '.':
                    number += int(i)
            mes = str(number)
        description = get_description(number)
        bot.send_message(message.chat.id, 'Ваше число судьбы: ' + str(number))

        bot.send_message(message.chat.id, description, parse_mode="HTML")
        user_states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод данных', parse_mode="HTML")


@bot.message_handler(commands=['day_birthday'])
def destiny_number(message):
    bot.send_message(message.chat.id,
                     'Введите день вашего рождения. Например, если у вас день рождения 17.05.1965, то отправьте 17')
    user_states[message.chat.id] = 'day_birthday'


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'day_birthday')
def get_birthday(message):
    if len(message.text.strip()) <= 2 and message.text.isnumeric():
        bot.send_message(message.chat.id, get_decode_birthday(int(message.text)))
        user_states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод данных', parse_mode="HTML")


@bot.message_handler(commands=['zodiac'])
def zodiak(message):
    bot.send_message(message.chat.id, 'Введите вашу дату рождения в формате дд.мм.гггг. Например, 20.08.2002')
    user_states[message.chat.id] = 'zodiac'


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'zodiac')
def get_birthday(message):
    match = re.search(r'\d{2}\.\d{2}\.\d{4}', message.text)
    if match:
        data = match.group()
        data = data.split('.')
        month = data[1]
        day = data[0]
        zodiac = get_zodiac(month, day)
        bot.send_message(message.chat.id, zodiac, parse_mode="HTML")
        user_states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод данных', parse_mode="HTML")


@bot.message_handler(commands=['value_name'])
def value_name(message):
    bot.send_message(message.chat.id,
                     'Введите ваше ФИО на русском языке через пробел. Например, Лушкин Валерьян Еванович')
    user_states[message.chat.id] = 'value_name'


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'value_name')
def get_value_name(message):
    if len(message.text.split(' ')) != 3:
        bot.send_message(message.chat.id, 'Неправильный ввод данных', parse_mode="HTML")
        return
    text = calculate_name(message.text)
    if text != -1:
        bot.send_message(message.chat.id, text, parse_mode="HTML")
        user_states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод данных', parse_mode="HTML")


@bot.message_handler(commands=['totem_animal'])
def get_totem_animal(message):
    bot.send_message(message.chat.id, 'Введите вашу дату рождения в формате гггг.мм.дд. Например, 20.08.2002')
    user_states[message.chat.id] = 'totem_animal'


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'totem_animal')
def get_totem_animal(message):
    match = re.search(r'\d{2}\.\d{2}\.\d{4}', message.text) #find 22.12.2002 in line
    if match: # if searching is successful
        data = match.group() #get date
        data = data.split('.')
        animal = totem_animal(data[0], data[1], data[2])
        bot.send_message(message.chat.id, animal, parse_mode="HTML")
        user_states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод данных', parse_mode="HTML")


@bot.message_handler(commands=['horoscope'])
def get_horoscope(message):
    bot.send_message(message.chat.id,
                     '<strong>Введите название знака зодиака:</strong>\n\nОвен, Телец, Близнецы, Рак, Лев, Дева, Весы, Скорпион, Стрелец, Козерог, Водолей, Рыбы',parse_mode='HTML')
    user_states[message.chat.id] = 'horoscope'


@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'horoscope')
def horoscope_handler(message):
    name = str(message.text)
    horoscope = get_horoscope_today(name)
    bot.send_message(message.chat.id, horoscope)


@bot.message_handler(content_types=['text'])
def error_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет! Чтобы узнать мои функции, воспользуйтесь командой /help')
    else:
        bot.send_message(message.chat.id, 'Непонятная команда🤨\n Чтобы посмотреть мои функции введите /help')

@bot.message_handler(content_types=['sticker'])
def handle_sticker(message):
    with open('astr.png','rb') as sticker:
        bot.send_sticker(message.chat.id, sticker)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            pass
