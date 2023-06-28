import telebot
from destiny_number import get_description
from date_birthday import get_decode_birthday
from number_name import calculate_name
import re

token = '6232507877:AAF5qdMgv0HAQHWMgggi8Nk1PDK6DOw4zho'
bot = telebot.TeleBot(token)
user_states = {}


def totem_animal(day, month, year):
    digit = (int(day) + int(month)) * int(year)
    line = str(digit)
    res = 0
    while len(line) > 1:
        res = 0
        for i in str(line):
            res = res + int(i)
        line = str(res)
    if res == 1:
        return 'Ваше тотемное животное: <strong>Слон</strong>🐘\n\nСлон предлагает своему обладателю перенять у него умение оберегать своих близких, заботится о них. \nЛюди с этим тотемным животным должны искать семейное счастье и любовь, ведь именно это наделит их удачей и полной поддержкой от своего «хранителя».\nТакже стоит отметить, что у людей с этим тотемным животным часто не хватает защитных рефлексов. Однако они компенсируют это своей стойкостью и неустанным поиском ответов на свои вопросы.'
    if res == 2:
        return 'Ваше тотемное животное: <strong>Тигр</strong>🐅\n\nТигр – это очень сильное и прекрасное тотемное животное, которое способно помощь своему обладателю во всех жизненных аспектах.\nГлавное правило Тигра «Прощать своего обидчика, но только после того, как обидчик полностью признал свое поражение».'
    if res == 3:
        return 'Ваше тотемное животное: <strong>Ворон</strong>🐤\n\nВорон считается мудрой, анализирующей все вокруг птицей, склонной так же и к самокритике и хитрости.\nИменно эти качества, она и передает своему обладателю.\nЛюди с этим тотемным животным склонны использовать свой разум, а не грубую силу.\nГлавное правило Ворона «Не использовать силу там, где можно использовать интеллект».'
    if res == 4:
        return 'Ваше тотемное животное: <strong>Дельфин</strong>🐬\n\nДельфин – это единственное тотемное животное, которое соединяет в себе все четыре стихии: землю, воду, огонь и воздух.\nОбладатели этого тотемного животного способны добиться невероятных успехов в любой сфере. Для этого им всего то необходимо сохранять собственные силы, а значит не растрачивать свои ресурсы на незначительные вещи, события и на негативных людей.'
    if res == 5:
        return 'Ваше тотемное животное: <strong>Собака</strong>🐶\n\nЭто тотемное животное дарит своему обладателю мотивацию, которая помогает правильно ставить цели и достигать их.\nСобака показывает путь к правильному месту в мире, а также помогает найти верных друзей и любовь.'
    if res == 6:
        return 'Ваше тотемное животное: <strong>Орел</strong>🦅\n\nОрел дарит человеку чувство свободы и независимости. Люди с эти тотемным животным очень редко чувствуют себя скованными, ведь свобода у них в крови.\nТакже орел помогает в правильной расстановке жизненных приоритетов. Однако стоит помнить, что если не поставить Орлу четкую цель, но не будет работать.'
    if res == 7:
        return 'Ваше тотемное животное: <strong>Змея</strong>🐍\n\nЭто тотемное животное, часто призывает своего обладателя к уединению. Однако оно помогает преодолевать трудности и препятствия.\nЗмея дарит человеку хорошее чутье, выносливость и стойкость. Но вот силу, к сожалению, подарить не может.'
    if res == 8:
        return 'Ваше тотемное животное: <strong>Кот</strong>🐈\n\nКот приносит своему обладателю везение в любовных делах, развивает интуицию, но не логику. Поэтому людям с этим тотемом необходимо постоянно чему-то учится.\nКот приносит удачу своему подопечному и наделяет его телесной выносливостью.'
    if res == 9:
        return 'Ваше тотемное животное: <strong>Бык</strong>🐂\n\nБык помогает своему обладателю не отступать от намеченной цели, даже тогда, когда все казалось бы уже пропало.\nЭто тотемное животное считается невероятно сильным хранителем, ведь оно работает не только с подсознанием человека, но и с самим сознанием. А еще, бык помогает своему подопечному легко находить выходы из конфликтных ситуаций и заводить правильные знакомства.'
    return 'Неверные данные'


def get_zodiac(month, day):
    if (int(day) >= 21 and int(month) == 3) or (int(day) <= 20 and int(month) == 4):
        return 'Ваш знак зодиака: <strong>Овен</strong>\n\n Стихия: <strong>огонь</strong>🔥'
    if (int(day) >= 21 and int(month) == 4) or (int(day) <= 20 and int(month) == 5):
        return 'Ваш знак зодиака: <strong>Телец</strong>\n\n Стихия: <strong>земля</strong>🌏'
    if (int(day) >= 21 and int(month) == 5) or (int(day) <= 21 and int(month) == 6):
        return 'Ваш знак зодиака: <strong>Близнецы</strong>\n\n Стихия: <strong>воздух</strong>💨'
    if (int(day) >= 22 and int(month) == 6) or (int(day) <= 22 and int(month) == 7):
        return 'Ваш знак зодиака: <strong>Рак</strong>\n\n Стихия: <strong>вода</strong>🌊'
    if (int(day) >= 23 and int(month) == 7) or (int(day) <= 22 and int(month) == 8):
        return 'Ваш знак зодиака: <strong>Лев</strong>\n\n Стихия: <strong>огонь</strong>🔥'
    if (int(day) >= 23 and int(month) == 8) or (int(day) <= 23 and int(month) == 9):
        return 'Ваш знак зодиака: <strong>Дева</strong>\n\n Стихия: <strong>земля</strong>🌏'
    if (int(day) >= 24 and int(month) == 9) or (int(day) <= 23 and int(month) == 10):
        return 'Ваш знак зодиака: <strong>Весы</strong>\n\n Стихия: <strong>воздух</strong>💨'
    if (int(day) >= 24 and int(month) == 10) or (int(day) <= 22 and int(month) == 11):
        return 'Ваш знак зодиака: <strong>Скорпион</strong>\n\n Стихия: <strong>вода</strong>🌊'
    if (int(day) >= 23 and int(month) == 11) or (int(day) <= 21 and int(month) == 12):
        return 'Ваш знак зодиака: <strong>Стрелец</strong>\n\n Стихия: <strong>огонь</strong>🔥'
    if (int(day) >= 22 and int(month) == 12) or (int(day) <= 20 and int(month) == 1):
        return 'Ваш знак зодиака: <strong>Козерог</strong>\n\n Стихия: <strong>земля</strong>🌏'
    if (int(day) >= 21 and int(month) == 1) or (int(day) <= 18 and int(month) == 2):
        return 'Ваш знак зодиака: <strong>Водолей</strong>\n\n Стихия: <strong>воздух</strong>💨'
    if (int(day) >= 19 and int(month) == 2) or (int(day) <= 20 and int(month) == 3):
        return 'Ваш знак зодиака: <strong>Рыбы</strong>\n\n Стихия: <strong>вода</strong>🌊'

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет✌️\nЯ телеграмм бот ZodiacWorks ")
    help_message(message)


@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id,
                     "Вот список моего функционала:\n1) расчёт числа судьбы /destiny_number\n2) день рождения в нумерологии /day_birthday\n3) узнать знак зодиака /zodiac")


@bot.message_handler(commands=['destiny_number'])
def destiny_number(message):
    bot.send_message(message.chat.id, 'Введите вашу дату рождения в формате дд.мм.гггг. Например, 27.12.2003')
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
    bot.send_message(message.chat.id, 'Введите ваш день рождения')
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
    bot.send_message(message.chat.id, 'Введите вашу дату рождения в формате гггг.мм.дд. Например, 20.08.2002')
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
    bot.send_message(message.chat.id, 'Введите ваше ФИО на русском языке через пробел. Например, Лушкин Валерьян Еванович')
    user_states[message.chat.id] = 'value_name'

@bot.message_handler(func=lambda message: user_states.get(message.chat.id) == 'value_name')
def get_value_name(message):
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
    match = re.search(r'\d{2}\.\d{2}\.\d{4}', message.text)
    if match:
        data = match.group()
        data = data.split('.')
        animal = totem_animal(data[0], data[1], data[2])
        bot.send_message(message.chat.id, animal, parse_mode="HTML")
        user_states[message.chat.id] = None
    else:
        bot.send_message(message.chat.id, 'Неправильный ввод данных', parse_mode="HTML")

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception:
            pass

