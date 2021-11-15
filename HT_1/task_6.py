def is_value_in_group(value, iterable):
    print(value in iterable)


if __name__ == "__main__":
    is_value_in_group(int(input('Please, input some value: ')),
                      (tuple(map(int, input('Input your list: ').split(',')))))


