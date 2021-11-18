"""
Написати скрипт, який пройдеться по списку, який складається із кортежів, і замінить для кожного кортежа останнє значення.
Список із кортежів можна захардкодити. Значення, на яке замінюється останній елемент кортежа вводиться користувачем.
Значення, введене користувачем, можна ніяк не конвертувати (залишити рядком). Кількість елементів в кортежу повинна бути різна.
Приклад списка котежів: [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
Очікуваний результат, якщо введено "100":
Expected Output: [(10, 20, "100"), (40, 50, 60, "100"), (80, "100"), ("100",)]
"""


def last_element_changer(list_for_change, target_value):
    changed_list = [(element[:-1] + (target_value, )) for element in list_for_change]
    return changed_list


if __name__ == '__main__':
    inputted_value = input('Please, input target value for changing last element in tuples ')
    our_list = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
    print(last_element_changer(our_list, inputted_value))
