"""1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій
      (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число;
      знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача -
      не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про
      це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)"""

import csv
import datetime
import json


class NegativeMeaning(Exception):
    pass


def finish(login):
    print('Thank you, good luck!')


def new_user(login):
    with open('users_data.csv', 'r', encoding='utf-8') as users:
        users = csv.DictReader(users)
        if login in users:
            print('Name is already registered, please try again with unique name')
            return False
    password = input(f'{login}, input your password here:')
    transactions = open(f'{login}_transaction.txt', 'w', encoding='utf-8')
    transaction = {'transaction': 'new_user',
                   'date': str(datetime.datetime.now()),
                   'balance_before': 0,
                   'balance_after': 0}
    transaction = json.dumps(transaction)
    transactions.write(f'{transaction}\n')
    balance = open(f'{login}_balance.txt', 'w', encoding='utf-8')
    balance.write('0')
    users = open('users_data.csv', 'a', encoding='utf-8')
    user = csv.writer(users)
    user.writerow([login, password])
    users.close()
    transactions.close()
    balance.close()
    start()


def authenticated(login):
    with open('users_data.csv', 'r', encoding='utf-8') as users:
        users = csv.DictReader(users)
        for user in users:
            if user['login'] == login:
                for attempt in range(3):
                    if user['password'] == input(f'Input your password, you have {3 - attempt} attempts '):
                        return True
                    else:
                        if attempt != 2:
                            print(f'Incorrect password, try again, you have {2 - attempt} attempts ')
                else:
                    print('Too many attempts')
                    return False
        else:
            print('Your name is incorrect, or you not registered, do you want to registrate in our system?')
            answer = input('If you want to registrate - input "yes", or press enter to exit ')
            if answer:
                new_user(login)
            else:
                return False


def show_balance(login):
    with open(f'{login}_balance.txt', 'r', encoding='utf-8') as balance:
        print(int(balance.readline()))
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
    summ = int(input('Input the amount you want to add '))
    if summ <= 0:
        raise NegativeMeaning()
    with open(f'{login}_balance.txt', 'r', encoding='utf-8') as balance:
        old_balance = int(balance.readline())
    new_balance = old_balance + summ
    with open(f'{login}_balance.txt', 'w', encoding='utf-8') as balance:
        balance.write(str(new_balance))
        with open(f'{login}_transaction.txt', 'a', encoding='utf-8') as transactions:
            transaction = {'transaction': f'adding {summ}',
                           'date': str(datetime.datetime.now()),
                           'balance_before': old_balance,
                           'balance_after': new_balance}
            transaction = json.dumps(transaction)
            transactions.write(f'{transaction}\n')
    print(f'Thank your for using our ATM, you add {summ}, and now your balance is {new_balance}')
    if input('do ypu want to continue (print yes or no)' ) == 'yes':
        menu(login)
    else:
        finish(login)


def withdraw_money(login):
    summ = int(input('Input the amount you want to withdraw '))
    if summ <= 0:
        raise NegativeMeaning()
    with open(f'{login}_balance.txt', 'r', encoding='utf-8') as balance:
        old_balance = int(balance.readline())
        if summ > old_balance:
            print(f'You don`t have enough money on the balance')
            if input('do you want to continue (print yes or no)') == 'yes':
                menu(login)
            else:
                exit(login)
        else:
            new_balance = old_balance - summ
    with open(f'{login}_balance.txt', 'w', encoding='utf-8') as balance:
        balance.write(str(new_balance))
        with open(f'{login}_transaction.txt', 'a', encoding='utf-8') as transactions:
            transaction = {'transaction': f'withdrawing {summ}',
                            'date': str(datetime.datetime.now()),
                            'balance_before': old_balance,
                            'balance_after': new_balance}
            transaction = json.dumps(transaction)
            transactions.write(f'{transaction}\n')
        print(f'Thank your for using our ATM, you withdraw {summ}, and now your balance is {new_balance}')
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
                   )
    choices = {
        '1': withdraw_money,
        '2': add_money,
        '3': show_balance,
        '4': finish

    }
    choices[choice](login)


def start():
    if input('Do you have an account? (print yes or no) ') == 'yes':
        login = input('Hello, please input your login: ')
        if authenticated(login):
            menu(login)
    else:
        if input('Do you want to register an account?(print yes or no) ') == 'yes':
            login = input('Input your login here ')
            new_user(login)


if __name__ == '__main__':
    try:
        start()
    except NegativeMeaning:
        print('You try to input negative meaning')
