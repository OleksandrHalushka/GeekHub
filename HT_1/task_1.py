def list_tuple_maker(sequence):
    sequence_list = sequence.split(',')
    sequence_tuple = tuple(sequence.split(','))
    print(f' List : {sequence_list} \n Tuple : {sequence_tuple}')


if __name__ == "__main__":
    list_tuple_maker(input('Input your sequence here :'))
