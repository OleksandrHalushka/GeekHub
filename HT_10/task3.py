"""
3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
"""

import datetime

import requests


def currency_exchange():
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={datetime.datetime.now().strftime("%d.%m.%Y")}'
    raw = requests.get(url)
    currencylist = raw.json()['exchangeRate']

    currency_choices = {'1': 'USD',
                        '2': 'EUR',
                        '3': 'PLN',
                        '4': 'GBP'}
    currency_choice = input(f'Choose what currency you want to exchange\n'
                            '1 for USD\n'
                            '2 for EUR\n'
                            '3 for PLZ\n'
                            '4 for GBP\n'
                            '5 for UAH\n'
                            )
    if currency_choice == '5':
        buying_rate = 1
        currency = 'UAH'
    else:
        currency = currency_choices[currency_choice]
        for next_currency in currencylist:
            if 'currency' in next_currency.keys():
                if next_currency["currency"] == currency:
                    buying_rate = next_currency['purchaseRate']

    value = int(input(f'Write how many {currency} you want to exchange: '))

    currency_choice = input(f'Choose which currency you want to exchange {value} {currency}\n'
                            '1 for USD\n'
                            '2 for EUR\n'
                            '3 for PLZ\n'
                            '4 for GBP\n'
                            '5 for UAH\n'
                            )
    if currency_choice == '5':
        selling_rate = 1
        currency_choice = 'UAH'
    else:
        currency_choice = currency_choices[currency_choice]
        for next_currency in currencylist:
            if 'currency' in next_currency.keys():
                if next_currency["currency"] == currency_choice:
                    selling_rate = next_currency['purchaseRate']
    if currency == currency_choice:
        print('Please select different currencies')
        if input('Do you want to continue? ') == 'yes':
            currency_exchange()
        else:
            exit()
    issue = value * (buying_rate / selling_rate)
    issue = f'{issue:.2f}'
    print(f'You exchanged {value} {currency} for {issue} {currency_choice}')
    if input('Do you want to continue? ') == 'yes':
        currency_exchange()
    else:
        exit()


if __name__ == '__main__':
    currency_exchange()
