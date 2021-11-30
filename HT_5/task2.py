"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :) #пароль не має співпадати з іменем#
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""


class LenNameException(Exception):
    pass


class PasswordLenException(Exception):
    pass


class NoDigitPasswordException(Exception):
    pass


class NameInPasswordException(Exception):
    pass


def name_password_validator(name, password):
    if 3 > len(name) >= 50:
        raise LenNameException
    if len(password) < 8:
        raise PasswordLenException
    if len(list(filter(str.isdigit, list(password)))) == 0:
        raise NoDigitPasswordException
    if name in password:
        raise NameInPasswordException
    return
