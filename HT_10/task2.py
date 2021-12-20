"""
2. Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
   - Перелік валют краще принтануть.
   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
   - Також перевірте, чи введена правильна валюта.
   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
   курсу обраної валюти (Нацбанк) від введеної дати до поточної. Приблизний вивід наступний:
   Currency: USD
   Date: 12.12.2021
   NBU:  27.1013   -------
   Date: 13.12.2021
   NBU:  27.0241   -0,0772
   Date: 14.12.2021
   NBU:  26.8846   -0,1395
"""
import datetime
from time import sleep

import requests


def dates_generator(date_from):
    date_to = datetime.datetime.now()
    while date_from <= date_to:
        yield date_from.strftime("%d.%m.%Y")
        date_from = date_from + datetime.timedelta(days=1)


def rate(currency, date):
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    raw = requests.get(url)
    currencylist = raw.json()['exchangeRate']
    for next_currency in currencylist:
        if 'currency' in next_currency.keys():
            if next_currency['currency'] == currency:
                return {'nbu': next_currency['saleRateNB'],
                        'buy': next_currency['purchaseRate'],
                        'sell': next_currency['saleRate']}


def rate_from():
    str_date = input('Input start date in format dd.mm.yyyy ')
    try:
        date_from = datetime.datetime.strptime(str_date, "%d.%m.%Y")
    except:
        print('Something wrong, maybe you wrote incorrect date, please, check your date')
        rate_from()
    else:
        if date_from > datetime.datetime.now():
            print('Your date later than now, please correct your date')
            rate_from()
        else:
            currency_choice = input('Please, select currency\n'
                                    '1 for USD\n'
                                    '2 for EUR\n'
                                    '3 for PLZ\n'
                                    '4 for GBP\n'
                                    )
            currency_choices = {'1': 'USD',
                                '2': 'EUR',
                                '3': 'PLN',
                                '4': 'GBP'}
            currency = currency_choices[currency_choice]
            delta = '---------------'
            last_rate = None
            for date in dates_generator(date_from):
                rates = rate(currency, date)
                if last_rate:
                    delta = (rates['nbu'] - last_rate)
                    delta = f'{delta:.4f}'
                print(date)
                print(f'NBU = {rates["nbu"]}      {delta}')
                print('-----------------------------------')
                last_rate = rates['nbu']
                sleep(0.5)
            if input('Do you want to continiue? ') == 'yes':
                rate_from()
            else:
                print('Thank you, good bye')
                exit()


if __name__ == '__main__':
    rate_from()
