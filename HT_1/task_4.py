def string_concatenation():
    number = int(input('Please, input some positive number '))
    if number <= 0:
        print('Oh, no! Please, input POSITIVE number!')
        string_concatenation()
    else:
        result = ''
        for string in range(number):
            result += input('Input your next string: ')
        print(result)


if __name__ == "__main__":
    string_concatenation()
