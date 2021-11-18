"""
Написати скрипт, який видалить пусті елементи із списка. Список можна "захардкодити".
Sample data: [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']
"""


def empty_element_cleaner(some_list):
    new_list = [element for element in some_list if element]
    return new_list


if __name__ == '__main__':
    old_list = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
    print(empty_element_cleaner(old_list))
