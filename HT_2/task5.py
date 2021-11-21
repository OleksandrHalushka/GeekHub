"""
Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). Словник для
роботи захардкодити свій.
        Приклад словника (не використовувати):
        {'a': 1, 'b': 3, 'c': 1, 'd': 5}
        Очікуваний результат:
        {'a': 1, 'b': 3, 'd': 5}
"""


def dictionary_cleaner(some_dictionary):
    cleaned_dictionary = {}
    our_keys = some_dictionary.keys()
    for index in our_keys:
        if some_dictionary[index] in cleaned_dictionary.values():
            continue
        else:
            cleaned_dictionary[index] = some_dictionary[index]
    return cleaned_dictionary


if __name__ == '__main__':
    strange_dictionary = {'a': 1, 'b': 3, 'c': [6, 7], 'd': 8, 'e': 9, 'f': 11, 'g': 3, 'h': 4, 'i': 5, 'j': 4, 'k': 2,
                          'l': 3, 'm': 1, 'n': 8, 'o': [6, 7], 'p': 9, 'q': 4, 'r': 4, 's': 6, 't': 4, 'y': 1}

    print(dictionary_cleaner(strange_dictionary))
