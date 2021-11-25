""" 6. Вводиться число. Якщо це число додатне, знайти його квадрат, якщо від'ємне, збільшити його на 100,
якщо дорівнює 0, не змінювати. """


def some_magick(number):
    if number == 0:
        return 0
    elif number > 0:
        return number**2
    else:
        return number + 100


if __name__ == '__main__':
    print(some_magick(int(input('Input your number here '))))
