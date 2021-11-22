"""
Маємо рядок --> "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" ->
просто потицяв по клавi
   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""


def some_magick_function(some_string):  # Цю функцію по клінкоду мабуть не назвати
    letters = list(filter(str.isalpha, list(some_string)))
    numbers = list(map(int, (filter(str.isdigit, list(some_string)))))
    if len(some_string) < 30:
        print(sum(numbers), ''.join(letters), sep='\n')
    elif len(some_string) > 50:
        letters_counter = {}.fromkeys(set(letters), 0)
        for letter in letters:
            letters_counter[letter] += 1
        numbers_counter = {}.fromkeys(set(numbers), 0)
        for number in numbers:
            numbers_counter[number] += 1
        print('For this long line, I have sorted all alphabetic and numeric items from most common to rarest.\n'
              'I have no idea why I need this, but orderliness is great!')
        print(*sorted(letters_counter, key=letters_counter.get, reverse=True))
        print(*sorted(numbers_counter, key=numbers_counter.get, reverse=True))
    else:
        print(f'We have string with length {len(some_string)} symbols.\n'
              f'This string has {len(letters)} letters and {len(numbers)} numbers')


if __name__ == '__main__':
    print('Length more than 50 symbols:')
    some_magick_function(
        "f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345")
    print('\n Length from 30 to 50 symbols:')
    some_magick_function('f98neroi4nr0c3n30irn037kkj546p465jnpoj35po6j345')
    print('\n Length less than 30 symbols:')
    some_magick_function('f98neroi4nr0c3n30irn037kkj')
