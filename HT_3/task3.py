"""
3. Написати функцiю season, яка приймає один аргумент — номер мiсяця (вiд 1 до 12), яка буде повертати пору року,
якiй цей мiсяць належить (зима, весна, лiто або осiнь)
"""


def season_from_month():
    year = (('Winter', 1, 2, 12), ('Spring', 3, 4, 5), ('Summer', 6, 7, 8), ('Autumn', 9, 10, 11))
    month = int(input("Input number of month here to : "))
    if month in range(1, 13):
        for season in year:
            if month in season:
                print(season[0])
    else:
        print('Oh, are you not from Earth? We have 12 months on Earth!')
        season_from_month()


if __name__ == '__main__':
    season_from_month()
