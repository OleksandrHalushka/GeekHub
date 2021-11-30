"""1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий
   параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>,
       інакше (<silent> == <False>) - породжується виключення LoginException"""


class LoginException(Exception):
    pass


def user_validator(login, password, silent=False):
    user_list = [('user1', 'password1'), ('user2', 'password2'), ('user3', 'password3'),
                ('user4', 'password4'), ('user5', 'password5')]
    for user in user_list:
        if (login, password) == (user[0], user[1]):
            return True
    if silent:
        return False
    else:
        raise LoginException


if __name__ == '__main__':
    try:
        user_validator('user1', 'password1')
    except LoginException:
        print("login exception")
    else:
        print(user_validator('user1', 'password1'))

    try:
        user_validator('user1', 'password2')
    except LoginException:
        print("login exception")
    else:
        print(user_validator('user1', 'password2'))

    try:
        user_validator('user1', 'password2', silent=True)
    except LoginException:
        print("login exception")
    else:
        print(user_validator('user1', 'password2', silent=True))
