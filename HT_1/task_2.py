def colors_dont_repeat(first, second):
    new_set = (set(first) - set(second))
    return new_set


if __name__ == "__main__":
    color_list_1 = input('Please, input first set of colors ').split(', ')
    color_list_2 = input('Please, input second set of colors ').split(', ')
    print(colors_dont_repeat(color_list_1, color_list_2))
