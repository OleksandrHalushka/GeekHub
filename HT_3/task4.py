"""
4. Створiть 3 рiзних функцiї (на ваш вибiр). Кожна з цих функцiй повинна повертати якийсь результат.
Також створiть четверу ф-цiю, яка в тiлi викликає 3 попереднi, обробляє повернутий ними результат та також
повертає результат. Таким чином ми будемо викликати 1 функцiю, а вона в своєму тiлi ще 3
"""


def chinesean_horoscope(year):
    characters = {
        'Rat': range(1900, 2022, 12),
        'Bull': range(1901, 2022, 12),
        'Tiger': range(1902, 2022, 12),
        'Rabbit': range(1903, 2022, 12),
        'Dragon': range(1904, 2022, 12),
        'Snake': range(1905, 2022, 12),
        'Horse': range(1906, 2022, 12),
        'Goat': range(1907, 2022, 12),
        'Monkey': range(1908, 2022, 12),
        'Rooster': range(1909, 2022, 12),
        'Dog': range(1910, 2022, 12),
        'Pig': range(1911, 2022, 12)
    }
    for key, value in characters.items():
        if year in value:
            return key


def younger_than_me(year):
    if year > 1995:
        return "you are younger than me"
    elif year < 1995:
        return "you are older than me"
    else:
        return 'we are the same age'


def your_age(year):
    age = 2021 - year
    return f'You are {age} years old.'


def some_about_you():
    print("This simple function can say three facts about you!")
    year = int(input('Please, input year your born here: '))
    if 1903 <= year <= 2021:
        character = chinesean_horoscope(year)
        age = your_age(year)
        younger = younger_than_me(year)
        print(
            f'So, you was born in {year}.\n{age}\nYou character in chinesean horoscope '
            f'is {character} and {younger}. \nNice to meet you!'
        )
    else:
        print("I think you were wrong. Please try again")
        some_about_you()


if __name__ == '__main__':
    some_about_you()
