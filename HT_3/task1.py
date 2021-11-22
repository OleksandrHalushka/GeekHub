"""
1. Створити цикл від 0 до ... (вводиться користувачем). В циклі створити умову, яка буде виводити поточне значення,
якщо остача від ділення на 17 дорівнює 0.
"""


def is_divisible_by_seventeen(last_value):
    # I exclude zero from the range, because I think that the operation of dividing zero by a number in this example is
    # meaningless in this case
    for number in range(1, (last_value + 1)):
        if (number % 17) == 0:
            print(number)


if __name__ == '__main__':
    is_divisible_by_seventeen(int(input('Input last number in your range: ')))
