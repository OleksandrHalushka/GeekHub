"""
1. Написати функцію < square > , яка прийматиме один аргумент - сторону квадрата, і вертатиме 3 значення (кортеж):
 периметр квадрата, площа квадрата та його діагональ.
"""

from math import sqrt


def square(length):
    if length >= 0:
        perimeter = length * 4
        area = length**2
        diagonal = sqrt(area * 2)
        return perimeter, area, diagonal
    else:
        return 'Side length of square must be positive'


if __name__ == '__main__':
    users_lenght = float(input('Input side length of a square: '))
    print(square(users_lenght))
