"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній:
   https://docs.python.org/3/library/stdtypes.html#range
"""


class WrongDirectionException(Exception):
    pass


class ToManyArgsException(Exception):
    pass


class NoArgumentException(Exception):
    pass


def custom_range(*args):
    if not args:
        raise NoArgumentException
    if len(args) == 1:
        position = 0
        while position != args[0]:
            yield position
            if args[0] > 0:
                position += 1
            else:
                position -= 1
    elif len(args) == 2:
        position = args[0]
        while position != args[1]:
            yield position
            if args[0] < args[1]:
                position += 1
            else:
                position -= 1
    elif len(args) == 3:
        if (args[0] < args[1] and args[2] > 0) or (args[0] > args[1] and args[2] < 0):
            position = args[0]
            if position < args[1]:
                while position < args[1]:
                    yield position
                    position += args[2]
            else:
                while position > args[1]:
                    yield position
                    position += args[2]
        else:
            raise WrongDirectionException
    else:
        raise ToManyArgsException


if __name__ == '__main__':
    try:
        [print(i) for i in custom_range(10, -10)]
    except WrongDirectionException:
        print('Wrong direction, please, change last argument')
    except NoArgumentException:
        print('Please, input from 1 to 3 arguments')
    except ToManyArgsException:
        print('The maximum number of arguments is three')

