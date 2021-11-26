""" 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому."""\

from collections import Counter


def elements_counter(some_list):
    counter = Counter()
    for element in some_list:
        counter[element] += 1
    return counter


if __name__ == '__main__':
    our_list = ["a", "b", "c", "c", "c", "f", "f", "g", "r", "e", "t", "qq", 'f', "g", 'q', 'a', 'v', 'c']
    print(*elements_counter(our_list).most_common())
