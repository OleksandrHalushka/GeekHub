"""
Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""


def simple_calculator():
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '//': lambda x, y: x // y,
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y,
    }
    start = input('This is simple calculator with basic math operators.\n'
                  'You can input mathematical expression with two numbers and a mathematical operator between them\n'
                  'Arguments must be separated by spaces\n'
                  "Or you can input 'exit' for finish or 'help' to watch available actions.\n") or ' '
    if start == 'exit':
        print('Thanks, goodbye!')
    elif start == ' ':
        simple_calculator()
    elif start == 'help':
        print(*operators)
        simple_calculator()
    else:
        first_value, action, second_value = start.split()
        first_value = float(first_value)
        second_value = float(second_value)
        result = operators[action](first_value, second_value)
        if result.is_integer():
            print(int(result))
        else:
            (print(result))
        simple_calculator()


if __name__ == '__main__':
    simple_calculator()
