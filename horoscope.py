import requests
from bs4 import BeautifulSoup
zodiac = {'овен': 'aries', 'телец':'taurus','близнецы':'gemini', 'рак':'cancer','лев':'leo', 'дева':'virgo', 'весы':'libra', 'скорпион':'scorpio', 'стрелец':'sagittarius', 'козерог':'capricorn', 'водолей':'aquarius', 'рыбы':'pisces'}


def get_horoscope_today(name):
    name = str(name).lower()
    if zodiac.get(name) is None:
        return 'Неправильно введён знак зодиака'
    url = 'https://horo.mail.ru/prediction/' + zodiac[name] +'/today/'
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        block = soup.find('div', class_='article__item_html')
        if block:
            paragraphs = block.find_all('p')
            if paragraphs:
                content = ''
                for paragraph in paragraphs:
                    content += paragraph.get_text() + '\n\n'
                return content
    return 'Непредвиденная ошибка'