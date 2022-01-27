"""Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
Документація на АПІ:
https://github.com/HackerNews/API
Скрипт повинен отримувати із командного рядка одну із наступних категорій:
askstories, showstories, newstories, jobstories
Якщо жодної категорії не указано - використовувати newstories.
Якщо категорія не входить в список - вивести попередження про це і завершити роботу.
Результати роботи зберегти в CSV файл. Зберігати всі доступні поля. Зверніть увагу - інстанси різних типів мають
різний набір полів.
Код повинен притримуватися стандарту pep8.
Перевірити свій код можна з допомогою ресурсу http://pep8online.com/
"""

import requests
import csv
import datetime
import sys


class NewsFromApi(object):
    categories = ('askstories', 'showstories', 'newstories', 'jobstories')

    def __init__(self):
        try:
            self.category = sys.argv[1]
        except:
            self.category = 'newstories'

        if self.category not in self.categories:
            print('Incorrect category')
            exit()

    def get_news(self):
        url = f'https://hacker-news.firebaseio.com/v0/{self.category}.json'
        articles = requests.get(url).json()
        category_news = []
        header = set()
        for article in articles:
            url = f'https://hacker-news.firebaseio.com/v0/item/{article}.json'
            request = requests.get(url=url).json()
            if not request:
                continue
            else:
                category_news.append(request)
                header.update(request.keys())
        header = sorted(header)
        with open(f'{self.category}_'
                  f'{datetime.date.today().strftime("%Y_%m_%d")}.csv',
                  'w', encoding='utf-8', newline='') as file:
            write = csv.DictWriter(file, fieldnames=header, restval='None')
            write.writeheader()
            write.writerows(category_news)


if __name__ == '__main__':
    news = NewsFromApi()
    news.get_news()
