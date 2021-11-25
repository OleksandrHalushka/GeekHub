"""
5. Написати функцію < fibonacci >, яка приймає один аргумент і виводить всі числа Фібоначчі, що не перевищують його.
"""


def fibonacci(number):
    fibo = [0, 1, 1]
    if number == 0:
        return [0]
    elif number == 1:
        return fibo
    else:
        while fibo[-1] <= number:
            next_fibo = fibo[-2] + fibo[-1]
            if next_fibo <= number:
                fibo.append(next_fibo)
            else:
                return fibo


if __name__ == '__main__':
    print(*fibonacci(int(input('Input your number '))))
