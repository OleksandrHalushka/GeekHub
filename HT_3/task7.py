"""
Ну і традиційно -> калькулятор :) повинна бути 1 ф-цiя яка б приймала 3 аргументи - один з яких операцiя, яку зробити!
"""


def simple_calculator(last_result='None'):
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

        if start.split()[0].isdigit() and len(start.split()) == 3:
            first_value, action, second_value = start.split()
        elif last_result != 'None' and len(start.split()) == 2:
            first_value = last_result
            action, second_value = start.split()
        else:
            print('Something wrong')
            simple_calculator()
        first_value = float(first_value)
        second_value = float(second_value)
        if action in ('/', '//') and second_value == 0:
            print('Division by zero is not possible!')
            simple_calculator()
        result = operators[action](first_value, second_value)
        if result.is_integer():
            print(int(result))
            print(f'Now you can use {result} as first arg')
        else:
            (print(result))
            print(f'Now you can use {result} as first arg')
        simple_calculator(last_result=result)


if __name__ == '__main__':
    simple_calculator()
