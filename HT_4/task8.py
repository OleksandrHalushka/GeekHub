"""8. Написати функцію, яка буде реалізувати логіку циклічного зсуву елементів в списку. Тобто, функція приймає два
аргументи: список і величину зсуву (якщо ця величина додатня - пересуваємо з кінця на початок, якщо від'ємна -
навпаки - пересуваємо елементи з початку списку в його кінець). Наприклад: fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1,
2, 3, 4] fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2] """

# зробив дві функції, перша з яких може вертіти список безкінечно, але дуже важка, інша робить зсув в одну операцію


def cyclic_shift_steps(some_list, *, shift=0):
    our_list = some_list.copy()
    for i in range(abs(shift)):
        if shift > 0:
            our_list.insert(0, our_list[-1])
            our_list.pop(-1)
        if shift < 0:
            our_list.append(our_list[0])
            our_list.pop(0)
    return our_list


def cyclic_shift_fast(some_list, *, shift=0):
    shift = shift % len(some_list)
    return some_list[-shift:len(some_list) + 1] + some_list[0:-shift]


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    exepted_shift = int(input("Input expected shift here "))
    print(cyclic_shift_steps(my_list, shift=exepted_shift))
    print(cyclic_shift_fast(my_list, shift=exepted_shift))
