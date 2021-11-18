"""
Написати скрипт, який конкатенує всі елементи в списку і виведе їх на екран. Список можна "захардкодити".
Елементами списку повинні бути як рядки, так і числа.
"""


def string_from_list(some_list):
    elements_string = ''.join(map(str, some_list))
    return elements_string


if __name__ == '__main__':
    elements_list = ['This ', 'is ', 1, ' or ', 'not ', 1, ' maybe ', 2, ' or ', 1.21548]
    print(string_from_list(elements_list))
