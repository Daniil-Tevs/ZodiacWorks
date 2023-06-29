def get_zodiac(month, day):
    if int(day) < 1 or int(day) > 31:
        return 'День должен быть в пределах от 1 до 31'
    if int(month) < 1 or int(month) > 12:
        return 'Месяц должен быть в пределах от 1 до 12'
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
    return 'Error'