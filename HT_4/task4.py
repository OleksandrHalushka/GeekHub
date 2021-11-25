"""4. Написати функцію < prime_list >, яка прийматиме 2 аргументи - початок і кінець діапазона, і вертатиме список
простих чисел всередині цього діапазона. """

from math import sqrt


def is_prime(number):
    if number == 1:
        return False
    elif number == 2:
        return True
    else:
        for i in range(2, (int(sqrt(number)) + 1)):
            if (number % i) == 0:
                return False
        return True


def prime_list(start, stop):
    return list(filter(is_prime, range(start, stop + 1)))


if __name__ == '__main__':
    first = int(input('Input first number in your diapason '))
    last = int(input('Input last number in your diapason '))
    print(*prime_list(first, last))

