"""
1. Доповніть програму-банкомат наступним функціоналом:
   - новий пункт меню, який буде виводити поточний курс валют (API Приватбанк)
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
3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
P.S. Не забувайте про файл requirements.txt
P.P.S. Не треба сходу ДДОСить Приватбанк - додайте хоча б по 0.5 секунди між запросами.
       Хоч у них і не написано за троттлінг, але будьмо чемними ;)

"""



import sqlite3
import datetime
import json
from collections import Counter
import requests
from time import sleep

conn = sqlite3.connect('../../HT_9/task1/atm.db')
cur = conn.cursor()


class User:
    conn = sqlite3.connect('../../HT_9/task1/atm.db')
    cur = conn.cursor()

    def __init__(self, username):
        user = cur.execute(f"SELECT * FROM users WHERE username='{username}'").fetchone()
        self.__user = user
        self.__username = self.__user[1]
        self.__password = self.__user[2]
        self.__balance = self.__user[3]
        self.__status = self.__user[4]

    def get_username(self):
        return self.__username

    def get_password(self):
        return self.__password

    def get_balance(self):
        return int(self.__balance)

    def get_status(self):
        return self.__status

    def change_balance(self, change):
        new_balance = self.__balance + change
        cur.execute(f"UPDATE users SET balance = {new_balance} WHERE username = '{self.__username}'")
        conn.commit()

    def change_password(self, new_password):
        cur.execute(f"UPDATE users SET password = '{new_password}' WHERE username = '{self.__username}'")
        conn.commit()

    def block(self):
        cur.execute(f"UPDATE users SET status = 'Blocked' WHERE username = '{self.__username}'")
        conn.commit()

    def unblock(self):
        cur.execute(f"UPDATE users SET status = 'Active' WHERE username = '{self.__username}'")
        conn.commit()


class Atm:
    conn = sqlite3.connect('../../HT_9/task1/atm.db')
    cur = conn.cursor()

    def __init__(self):
        atm = cur.execute('SELECT * FROM denominations;').fetchall()
        self.__denominations = {
            atm[0][0]: int(atm[0][1]),
            atm[1][0]: int(atm[1][1]),
            atm[2][0]: int(atm[2][1]),
            atm[3][0]: int(atm[3][1]),
            atm[4][0]: int(atm[4][1]),
            atm[5][0]: int(atm[5][1]),
            atm[6][0]: int(atm[6][1]),
        }

    def get_denominations(self):
        return self.__denominations

    def change(self, new_values: dict):
        for value in new_values:
            cur.execute(f"UPDATE denominations SET count = '{new_values[value]}' WHERE denomination = '{value}'")
        conn.commit()


class NegativeMeaning(Exception):
    pass


def create_db():
    conn = sqlite3.connect('../../HT_9/task1/atm.db')
    cur = conn.cursor()
    if input('Would you like to create database? (yes/no)') == 'yes':
        fop = open('../../HT_9/task1/atm.db', 'w')
        fop.close()
        cur.execute("""CREATE TABLE IF NOT EXISTS users(
               user_id INT PRIMARY KEY,
               username TEXT,
               password TEXT,
               balance INT,
               status TEXT)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS denominations (
               denomination INT PRIMARY KEY,
               count INT)""")

        cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
              transaction_id INT PRIMARY KEY,
              operation TEXT,
              username TEXT)""")

        users = [('1', 'user1', 'user1', '1500', 'Active'),
                 ('2', 'user2', 'user2', '1500', 'Active'),
                 ('3', 'admin', 'admin', '0', 'Collector')
                 ]
        denominations = [(10, 100),
                         (20, 100),
                         (50, 100),
                         (100, 100),
                         (200, 100),
                         (500, 100),
                         (1000, 100)
                         ]
        cur.executemany("""INSERT INTO users VALUES(?,?,?,?,?);""", users)
        cur.executemany("""INSERT INTO denominations VALUES(?,?);""", denominations)
        cur.execute("""CREATE TABLE IF NOT EXISTS transactions (
                   id INT PRIMARY KEY,
                   operations TEXT)
                   """)
        conn.commit()


def password_validator():
    password_1 = input('Input your new password here: ')
    password_2 = input('Repeat new password: ')
    if password_1 == password_2:
        return password_1
    else:
        return password_validator()


def elements_counter(some_list):
    counter = Counter()
    for element in some_list:
        counter[element] += 1
    return counter.most_common()


def incasation(login):
    atm = Atm()
    money_in = atm.get_denominations()
    addmoney = money_in.copy()
    for denomination in money_in:
        add = int(input(f'Print count denomination {denomination}: '))
        if add < 0:
            raise NegativeMeaning('You can`t add negative count of money :)')
        addmoney[denomination] += add
    atm.change(addmoney)
    print('Money loaded successfully!')
    collectors_menu(login)


def checking_denominations(login):
    atm = Atm()
    money_in = atm.get_denominations()
    for denomination in money_in:
        print(f'{denomination}: {money_in[denomination]}')
    collectors_menu(login)


def finish(login):
    print('Thank you, good luck!')
    exit()


def blocker(login):
    user = User(login)
    if user.get_status() == 'Collector':
        finish(login)
    else:
        user.block()
        print('Your account was blocked')
        finish(login)


def unblocker(login):
    user = User(login)
    print('To unlock your account, answer the secret question: ')
    answer = input('What is the best programming language is the best? ')
    if answer == 'python' or 'Python':
        user.unblock()
        print('Account unlocked!')
        start()
    else:
        print('Sorry, answer is incorrect, try again later!')


def new_user(login):
    conn = sqlite3.connect('../../HT_9/task1/atm.db')
    cur = conn.cursor()
    users = cur.execute(f"SELECT username FROM users").fetchall()
    for user in users:
        if user[0] == login:
            print(f'Name {login} was already taken')
            finish(login)
    password = password_validator()
    transaction = {'transaction': 'new_user',
                   'date': str(datetime.datetime.now()),
                   'balance_before': 0,
                   'balance_after': 0}
    transaction = json.dumps(transaction)
    cur.execute("INSERT INTO transactions (operation, username)  VALUES (?, ?)", (transaction, login))
    cur.execute("INSERT INTO users (username, password, balance, status) VALUES (?, ?, ?, ?)",
                (login, password, '0', 'Active'))
    conn.commit()
    start()


def authenticated(login):
    user = User(login)
    for attempt in range(3):
        if user.get_password() == input(f'Input your password, you have {3 - attempt} attempts '):
            return True
        else:
            if attempt != 2:
                print(f'Incorrect password, try again, you have {2 - attempt} attempts ')
            else:
                print('Too many attempts')
                return blocker(login)


def show_balance(login):
    user = User(login)
    print(user.get_balance())
    choise = input('What do you want to do next?\n'
                   '1 for withdraw money\n'
                   '2 to Add money on your account\n'
                   '3 to exit\n')
    choises = {
        '1': withdraw_money,
        '2': add_money,
        '3': finish
    }
    return choises[choise](login)


def add_money(login):
    user = User(login)
    summ = int(input('Input the amount you want to add '))
    old_balance = user.get_balance()
    if summ < 0:
        raise NegativeMeaning()
    user.change_balance(summ)
    user = User(login)
    new_balance = user.get_balance()
    transaction = {'transaction': f'adding {summ}',
                    'date': str(datetime.datetime.now()),
                    'balance_before': old_balance,
                    'balance_after': new_balance}
    transaction = json.dumps(transaction)
    cur.execute("INSERT INTO transactions (operation, username)  VALUES (?, ?)", (transaction, login))
    conn.commit()
    print(f'Thank your for using our ATM, you add {summ}, and now your balance is {new_balance}')
    if input('do ypu want to continue (print yes or no)') == 'yes':
        menu(login)
    else:
        finish(login)


def withdraw_money(login):
    user = User(login)
    atm = Atm()
    money_in = atm.get_denominations()
    summ_in = 0
    for denomination in money_in:
        if int(money_in[denomination]) != 0:
            print(f'{denomination}', end=' ')
            summ_in += int(money_in[denomination]) * int(denomination)
    print(f'\nYou can take {summ_in}')
    print(f'You have {user.get_balance()} on your account')
    summ = int(input('Input the amount you want to withdraw '))
    if summ <= 0:
        raise NegativeMeaning()
    if summ_in < summ:
        print(f'ATM doesn`t have enough money')
        if input('do you want to continue (print yes or no)') == 'yes':
            menu(login)
        else:
            finish(login)
    old_balance = user.get_balance()
    if summ > old_balance:
        print(f'You don`t have enough money on the balance')
        if input('do you want to continue (print yes or no)') == 'yes':
            menu(login)
        else:
            finish(login)
    denominations_give = []
    money_after_give = money_in.copy()
    summ_to_give = summ
    iterlist = list(money_in.keys())
    iterlist.sort(key=lambda x: int(x), reverse=True)
    while summ_to_give > 0:
        for denomination in iterlist:
            if int(money_after_give[denomination]) != 0 and summ_to_give % int(denomination) == 0:
                summ_to_give -= int(denomination)
                denominations_give.append(int(denomination))
                money_after_give[denomination] -= 1
            else:
                continue
            break
        else:
            print('ATM can`t give you that summ')
            if input('do you want to continue (print yes or no)') == 'yes':
                menu(login)
            else:
                finish(login)
                break
    user.change_balance(-summ)
    user = User(login)
    new_balance = user.get_balance()
    transaction = {'transaction': f'withdrawing {summ}',
                    'date': str(datetime.datetime.now()),
                    'balance_before': old_balance,
                    'balance_after': new_balance}
    transaction = json.dumps(transaction)
    cur.execute("INSERT INTO transactions (operation, username)  VALUES (?, ?)", (transaction, login))
    conn.commit()
    print(f'You received')
    for element in elements_counter(denominations_give):
        print(f'{element[0]} - {element[1]} bills')
    print(f'Thank your for using our ATM, you withdraw {summ}, and now your balance is {new_balance}')
    atm.change(money_after_give)
    if input('do ypu want to continue (print yes or no) ') == 'yes':
        menu(login)
    else:
        finish(login)


def menu(login):
    choice = input('if you want:\n'
                   'Withdraw money - press 1\n'
                   'Add money on your account - press 2\n'
                   'Check your account - press 3\n'
                   'For exit press 4\n'
                   'For changing password press 5\n'
                   )
    choices = {
        '1': withdraw_money,
        '2': add_money,
        '3': show_balance,
        '4': finish,
        '5': change_password

    }
    choices[choice](login)


def change_password(login):
    if authenticated(login):
        new_password = password_validator()
        user = User(login)
        user.change_password(new_password)
        print('Your password was changed!')
        if input('Do you want to continue? (yes/no)') == 'yes':
            menu(login)
        else:
            finish(login)


def collectors_menu(login):
    choice = input('if you want:\n'
                   'add money in atm 1\n'
                   'check for denominations in ATM - press 2\n'
                   'For exit press 3\n'
                   )
    choices = {
        '1': incasation,
        '2': checking_denominations,
        '3': finish,
    }
    choices[choice](login)


def dates_generator(date_from):
    date_to = datetime.datetime.now()
    while date_from <= date_to:
        yield date_from.strftime("%d.%m.%Y")
        date_from = date_from + datetime.timedelta(days=1)


def rate(currency, date=None):
    if date is None:
        date = datetime.datetime.now().strftime("%d.%m.%Y")
    url = f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}'
    raw = requests.get(url)
    currencylist = raw.json()['exchangeRate']
    for next_currency in currencylist:
        if 'currency' in next_currency.keys():
            if next_currency['currency'] == currency:
                return {'nbu': next_currency['saleRateNB'],
                        'buy': next_currency['purchaseRate'],
                        'sell': next_currency['saleRate']}


def today_rate(currency, date=datetime.datetime.now().strftime("%d.%m.%Y")):
    rate_dict = rate(currency)
    print(f'Buy - {rate_dict["buy"]}\n'
          f'Purchase - {rate_dict["sell"]}\n'
          f'Nbu - {rate_dict["nbu"]}\n'
          f'-------------------')
    if input('Do you want to continiue? ') == 'yes':
        start()
    else:
        finish('')


def rate_from(currency):
    day = input('Input day like xx ')
    month = input('input month like xx (01, 12 ... 10, 11) ')
    corrected_month = month.rjust(2, '0')
    year = input('input year like xxxx ')
    str_date = day + corrected_month + year
    date_from = datetime.datetime.strptime(str_date, "%d%m%Y")
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
        start()
    else:
        finish('')


def currency_exchange(currency):
    value = int(input(f'Write how many {currency} you want to exchange: '))

    currency_choice = input(f'Choose which currency you want to exchange {value} {currency}\n'
                            '1 for USD\n'
                            '2 for EUR\n'
                            '3 for PLZ\n'
                            '4 for GBP\n'
                            '5 for UAH\n'
                            )
    currency_choices = {'1': 'USD',
                        '2': 'EUR',
                        '3': 'PLN',
                        '4': 'GBP'}
    buying_rate = rate(currency)['buy']
    if currency_choice == '5':
        selling_rate = 1
        currency_choice = 'UAH'
    else:
        selling_rate = rate(currency_choices[currency_choice])["sell"]
        currency_choice = currency_choices[currency_choice]
    issue = value * (buying_rate / selling_rate)
    issue = f'{issue:.2f}'

    print(f'You exchanged {value} {currency} for {issue} {currency_choice}')
    if input('Do you want to continiue? ') == 'yes':
        start()
    else:
        finish('')


def foreign_exchange_menu():
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
    choice = input('For today exchange rates press 1, \n'
                   'For everyday rate from some date press 2, \n'
                   'For exchange currency press 3 \n'
                   'For exit press 4\n')

    choices = {'1': today_rate,
               '2': rate_from,
               '3': currency_exchange,
               '4': finish}
    choices[choice](currency_choices[currency_choice])


def start():
    if input('Do you want to exchange money? ') == 'yes':
        foreign_exchange_menu()
    else:
        if input('Do you have an account? (print yes or no) ') == 'yes':
            login = input('Hello, please input your login: ')
            try:
                user = User(login)
            except:
                if input('User not found, do you want to continue? (yes/no)') == 'yes':
                    start()
                else:
                    finish(login)
            else:
                user = User(login)
                user_status = user.get_status()
                if user_status == 'Active':
                    if authenticated(login):
                        menu(login)
                if user_status == 'Collector':
                    if authenticated(login):
                        collectors_menu(login)
                if user_status == 'Blocked':
                    if input('Your account was blocked, do you want to try to unblock? (yes / no )') == 'yes':
                        unblocker(login)

        else:
            if input('Do you want to register an account?(print yes or no) ') == 'yes':
                login = input('Input your login here ')
                new_user(login)
            else:
                finish('smth')


if __name__ == '__main__':
    start()
