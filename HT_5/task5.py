"""
Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), сума цифр кожного елемент якого буде дорівнювати 10.
Перевірка: [19, 28, 37, 46, 55, 64, 73, 82, 91]
"""

my_list = [number for number in range(100) if sum(map(int, list(str(number)))) == 10]

if __name__ == '__main__':
    print(my_list)