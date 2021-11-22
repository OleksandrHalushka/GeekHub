"""
2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, який виведе всі високосні роки в цьому проміжку
(границі включно).
"""


def is_leap(year):
    leap = False
    if year % 4 == 0:
        leap = True
        if year % 100 == 0 and year % 400 != 0:
            leap = False
    return leap


def print_leaps(year_from, year_to):
    if len(list(filter(is_leap, range(year_from, year_to + 1)))):
        print(f'Leap years in range from {year_from} to {year_to}:')
        for year in filter(is_leap, range(year_from, year_to + 1)):
            print(year)
    else:
        print(f"Range from {year_from} to {year_to} don't have leap years.")


if __name__ == '__main__':
    first = int(input('Input first year in your range: '))
    last = int(input('Input last year in your range(inclusively): '))
    print_leaps(first, last)
