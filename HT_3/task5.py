"""
5. Користувач вводить змiннi "x" та "y" з довiльними цифровими значеннями;
-  Створiть просту умовну конструкцiю(звiсно вона повинна бути в тiлi ф-цiї), пiд час виконання якої буде перевiрятися
рiвнiсть змiнних "x" та "y" і при нерiвностi змiнних "х" та "у" вiдповiдь повертали рiзницю чисел.
-  Повиннi опрацювати такi умови:
-  x > y;       вiдповiдь - х бiльше нiж у на z
-  x < y;       вiдповiдь - у бiльше нiж х на z
-  x == y.      вiдповiдь - х дорiвнює z
"""


def comparison_values(x, y):
    if x == y:
        print(x, 'дорівнює', y)
    elif x > y:
        print(x, 'більше', y, f'на {x - y}')
    else:
        print(y, 'більше', x, f'на {y - x}')


if __name__ == '__main__':
    x, y = int(input('Input first value here ')), int(input('Input second value here '))
    comparison_values(x, y)
