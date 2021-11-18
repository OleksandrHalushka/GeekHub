"""
Написати скрипт, який отримає максимальне і мінімальне значення із словника. Дані захардкодити.
                Приклад словника (можете використовувати свій):
                dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
                Вихідний результат:
                MIN: 10
                MAX: 60
"""


def extremum_of_dictionary(some_dictionary):
    maximal = max(some_dictionary.values())
    minimal = min(some_dictionary.values())
    return f'MIN: {minimal} \nMAX: {maximal}'


if __name__ == '__main__':
    dict_1 = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80, 9: 90}
    print(extremum_of_dictionary(dict_1))
