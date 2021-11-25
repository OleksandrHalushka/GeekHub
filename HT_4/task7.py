""" 7. Написати функцію, яка приймає на вхід список і підраховує кількість однакових елементів у ньому."""

# бібліотеку collections не використвував, бо не вказано, що елемент списку обов"язково незмінним
# також не дуже очевидно, чи треба порахувати кількість елементів, що зустрічаються більше разу, чи частоту повторень
# тому рахую і те і інше


def elements_counter(some_list):
    unique_list = []
    for element in some_list:
        if element not in unique_list:
            unique_list.append([element, 1])
    for i in range(len(unique_list)):
        for trash in some_list:
            if unique_list[i][0] == trash:
                unique_list[i][1] += 1

    unique_list.sort(key=lambda x: x[1], reverse=True)
    countered_list = list(filter(lambda x: x[1] > 1, unique_list))
    if len(countered_list) == 0:
        print('Oll elements are unique')
    elif len(countered_list) == 1:
        print('There is one repeating element')
    else:
        print(f'There are {len(countered_list)} repeating elements')
    for element in countered_list:
        print(f'{element[0]} is repeated {element[1]} times')


if __name__ == '__main__':
    our_list = ['', 'adsdd', (1, 2,), 'sdsadasdasd', (1, 6, 8), ["a", "b", "c", "d"], {"key": "value"}, 'd',
                'sadsda', (1, 2,), ["a", "b", "c", "d"], {"key": "value"}, 'd', 'sdsadasdasd', '', 'adsdd', (1, 2,),
                'sdsadasdasd', (1, 6, 8), ["a", "b", "c", "d"], {"key": "value"}, 'd',
                'sadsda', (1, 2,), ["a", "b", "c", "d"], {"key": "value"}, 'd', 'sdsadasdasd', '', 'adsdd', (1, 2,),
                'sdsadasdasd', (1, 6, 8), ["a", "b", "c", "d"], {"key": "value"}, 'd',
                'sadsda', (1, 2,), ["a", "b", "c", "d"], {"key": "value"}, 'd', 'sdsadasdasd', 1, 5185, 'a', 'we']
    elements_counter(our_list)
