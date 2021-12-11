"""
Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку
   кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна
   кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається
   спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або
   не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,
   банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й,
   наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
2. Для кращого засвоєння - перед написанням коду із п.1 - видаліть код для старої програми-банкомату і напишіть весь
    код наново (завдання на самоконтроль).
    До того ж, скоріш за все, вам прийдеться і так багато чого переписати.
"""
# кажу чесно, завдання на самоконтроль провалив, використав функціонал попереднього АТМ, не від ліні а від нестачі часу
# прошу зрозуміти і пробачити
# якщо буде досить часу на вихідних - відрефакторю застосунок
# а поки мені спокійно що від працює

import csv
import datetime
import json
from collections import Counter


class NegativeMeaning(Exception):
    pass


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
    with open('money_in.txt', 'r', encoding='utf-8') as money_in:
        money_in = money_in.readline()
        money_in = json.loads(money_in)
        for denomination in money_in:
            add = int(input(f'Print count denomination {denomination}: '))
            if add <= 0:
                raise NegativeMeaning('You can`t add negative count of money :)')
            money_in[denomination] += add
    with open('money_in.txt', 'w', encoding='utf-8') as load_money:
        money_in = json.dumps(money_in)
        load_money.write(money_in)
    print('Money loaded successfully!')
    collectors_menu(login)


def checking_denominations(login):
    with open('money_in.txt', 'r', encoding='utf-8') as money_in:
        money_in = money_in.readline()
        money_in = json.loads(money_in)
        for denomination in money_in:
            print(f'{denomination}: {money_in[denomination]}')
    collectors_menu(login)


def finish(login):
    print('Thank you, good luck!')
    exit()


def blocker(login):
    status = open(f'{login}_status.txt', 'r', encoding='utf-8')
    users_status = status.readline().rstrip()
    status.close()
    if users_status == 'Collector':
        finish(login)
    else:
        status = open(f'{login}_status.txt', 'w', encoding='utf-8')
        status.write('Blocked')
        status.close()
        print('Your account was blocked')
        finish(login)


def unblocker(login):
    print('To unlock your account, answer the secret question: ')
    answer = input('What is the best programming language is the best? ')
    if answer == 'python' or 'Python':
        status = open(f'{login}_status.txt', 'w', encoding='utf-8')
        status.write('Active')
        status.close()
        print('Account unlocked!')
        start()
    elif answer == 'js' or 'javascript' or 'JS' or 'Javascript':
        balance = open(f'{login}_balance.txt', 'w', encoding='utf-8')
        balance.write('0')
        balance.close()
        print('WTF? Your balance was reset')
        finish(login)
    else:
        print('Sorry, answer is incorrect, try again later!')


def new_user(login):
    with open('users_data.csv', 'r', encoding='utf-8') as users:
        users = csv.DictReader(users)
        for user in users:
            if user['login'] == login:
                print('Name is already registered, please try again with unique name')
                return False
    password = password_validator()
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
    status = open(f'{login}_status.txt', 'w', encoding='utf-8')
    status.write('Active')
    user = csv.writer(users)
    user.writerow([login, password])
    users.close()
    transactions.close()
    balance.close()
    status.close()
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
                    return blocker(login)
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
    summ_in = 0
    with open('money_in.txt', 'r', encoding='utf-8') as money_in:
        money_in = money_in.readline()
        money_in = json.loads(money_in)
        print('There is denominations in our ATM:')
        for denomination in money_in:
            if int(money_in[denomination]) != 0:
                print(f'{denomination}', end=' ')
                summ_in += int(money_in[denomination]) * int(denomination)
        print(f'\nYou can take {summ_in}')
    summ = int(input('Input the amount you want to withdraw '))
    if summ <= 0:
        raise NegativeMeaning()
    if summ_in < summ:
        print(f'ATM doesn`t have enough money')
        if input('do you want to continue (print yes or no)') == 'yes':
            menu(login)
        else:
            finish(login)
    with open(f'{login}_balance.txt', 'r', encoding='utf-8') as balance:
        old_balance = int(balance.readline())
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
        print(f'You received')
        for element in elements_counter(denominations_give):
            print(f'{element[0]} - {element[1]} bills')
        print(f'Thank your for using our ATM, you withdraw {summ}, and now your balance is {new_balance}')
        with open('money_in.txt', 'w', encoding='utf-8') as money_in:
            money_after_give = json.dumps(money_after_give)
            money_in.write(money_after_give)
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
        with open('users_data.csv', 'r', encoding='utf-8') as users:
            users = csv.DictReader(users)
            new_users = [user for user in users]
            for user in new_users:
                if user['login'] == login:
                    user['password'] = new_password
        with open('users_data.csv', 'w', encoding='utf-8') as users:
            user_writer = csv.DictWriter(users, fieldnames=['login', 'password'])
            user_writer.writeheader()
            for new_user in new_users:
                user_writer.writerow(new_user)
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


def start():
    if input('Do you have an account? (print yes or no) ') == 'yes':
        login = input('Hello, please input your login: ')
        status = open(f'{login}_status.txt', 'r', encoding='utf-8')
        user_status = status.readline().rstrip()
        status.close()
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


if __name__ == '__main__':
    try:
        start()
    except NegativeMeaning:
        print('You try to input negative meaning')
