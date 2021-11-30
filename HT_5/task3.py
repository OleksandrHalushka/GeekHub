"""
 На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні,
   так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для
   кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
"""


class ShortNameException(Exception):
    pass


class LongNameException(Exception):
    pass


class PasswordLenException(Exception):
    pass


class NoDigitPasswordException(Exception):
    pass


class NameInPasswordException(Exception):
    pass


def name_password_validator(name, password):
    if len(name) < 3:
        raise ShortNameException
    elif len(name) > 50:
        raise LongNameException
    elif len(password) < 8:
        raise PasswordLenException
    elif len(list(filter(str.isdigit, list(password)))) == 0:
        raise NoDigitPasswordException
    elif name in password:
        raise NameInPasswordException
    return


if __name__ == '__main__':
    try_dict = {
        'al': 'password',
        'alex': 'alex1alex',
        'alex12': 'thisisgood1password',
        'somename': 'somepassword',
        'somename12': 'pass',
        'oh_my_god_why_this_name_is_so_long?_Because_we_need_try_more_than_50_symbols_name!_But_who_can_make_this_username_in_real_life?': 'password1',
        'bestname': 'bestnamepassword1',
        'bestname_with_1': 'bestnamepassword',
        'good_username': 'good1password!'
    }
    for name in try_dict:
        try:
            name_password_validator(name, try_dict[name])
        except ShortNameException:
            print(f'Name: {name},\nPassword: {try_dict[name]}\nStatus: Name is too short')
        except LongNameException:
            print(f'Name: {name},\nPassword: {try_dict[name]}\nStatus: Name is too long')
        except PasswordLenException:
            print(f'Name: {name},\nPassword: {try_dict[name]}\nStatus: Password too short')
        except NoDigitPasswordException:
            print(f'Name: {name},\nPassword: {try_dict[name]}\nStatus: There is no digits in password')
        except NameInPasswordException:
            print(f'Name: {name},\nPassword: {try_dict[name]}\nStatus: There is name {name} in password')
        else:
            print(f'Name: {name},\nPassword: {try_dict[name]}\nStatus: OK')
        finally:
            print('_______________________________________')
