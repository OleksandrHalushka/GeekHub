def decimal_to_hexadecimal(decimal):
    hexadecimal = hex(decimal)
    return f'{hexadecimal}'[2:]


if __name__ == "__main__":
    print(decimal_to_hexadecimal(int(input('Please, input here some decimal '))))
