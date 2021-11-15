def sum_integers():
    number = int(input('Please, input some positive number '))
    if number < 0:
        print('Oh, no! Please, input POSITIVE number ')
        sum_integers()
    else:
        result = 0
        for element in range(number + 1):
            result += element
        print(result)


if __name__ == "__main__":
    sum_integers()
