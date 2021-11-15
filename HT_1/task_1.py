if __name__ == "__main__":
    sequence = input()
    sequence_list = sequence.split(',')
    sequence_tuple = tuple(sequence.split(','))
    print(f' List : {sequence_list} \n Tuple : {sequence_tuple}')

