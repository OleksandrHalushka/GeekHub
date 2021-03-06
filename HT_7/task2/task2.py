"""
2. Написати функцію, яка приймає два параметри: ім'я файлу та кількість символів.
   На екран повинен вивестись список із трьома блоками - символи з початку, із середини та з кінця файлу.
   Кількість символів в блоках - та, яка введена в другому параметрі.
   Придумайте самі, як обробляти помилку, наприклад, коли кількість символів більша, ніж є в файлі
   (наприклад, файл із двох символів і треба вивести по одному символу, що виводити на місці середнього блоку символів?)
   В репозиторій додайте і ті файли, по яким робили тести.
   Як визначати середину файлу (з якої брать необхідні символи) - кількість
   символів поділити навпіл, а отримане "вікно" символів відцентрувати щодо середини файла і взяти необхідну кількість.
   В разі необхідності заокруглення одного чи обох параметрів - дивіться на свій розсуд.
   Наприклад:
   █ █ █ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ ░ █ █ █    - правильно
                     ⏫ центр
   █ █ █ ░ ░ ░ ░ ░ ░ █ █ █ ░ ░ ░ ░ █ █ █    - неправильно
                     ⏫ центр

"""

# Центральний зріз  в випадку неспівпадіння парний / непарний тяжіє вліво.
# Інші варіанти (зменшення/збільшення центрального зрізу) - здались ще більш невірними(
# В зрізу більшого за файл вилітає екзепшн


class TooBigAmount(Exception):
    pass


def symbols_parser(file, amount):
    with open(file, 'r', encoding='utf-8') as file:
        string = file.read().rstrip('\n')
    if amount > len(string):
        raise TooBigAmount
    left_part = string[0:amount]
    right_part = string[-amount:]
    if amount % 2 == 0:
        central_part = string[(len(string)//2 - amount//2):(len(string)//2 + amount//2)]
    else:
        central_part = string[(len(string) // 2 - amount // 2):(len(string) // 2 + amount // 2 + 1)]
    print([left_part, central_part, right_part])


if __name__ == '__main__':
    try:
        symbols_parser('case3.txt', 11)
    except TooBigAmount:
        print('Your section is bigger than your file')

