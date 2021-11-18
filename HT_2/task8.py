"""
Написати скрипт, який отримує від користувача позитивне ціле число і створює словник, з ключами від 0 до введеного числа
а значення для цих ключів - це квадрат ключа.
Приклад виводу при введеному значенні 5 :
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
"""


def dictionary_of_squares(size):
    dictionary = {i: i**2 for i in range(size + 1)}
    return dictionary


if __name__ == '__main__':
    print(dictionary_of_squares(int(input('input size of your dictionary '))))
