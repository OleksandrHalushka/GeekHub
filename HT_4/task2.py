"""2. Написати функцію < bank > , яка працює за наступною логікою: користувач робить вклад у розмірі < a > одиниць
строком на < years > років під < percents > відсотків (кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році на них також нараховуються відсотки). Параметр < percents > є
необов'язковим і має значення по замовчуванню < 10 > (10%). Функція повинна принтануть і вернуть суму, яка буде на
рахунку. """


def bank(a, years, percents=10):
    for year in range(years):
        a = a * (1 + (percents / 100))
    print("%.2f" % a)
    return a


if __name__ == '__main__':
    money = float(input('Input your initial amount: '))
    period = int(input('Input your period in years '))
    interest_rate = input('Input your interest rate or press enter ') or 10
    interest_rate = float(interest_rate)
    bank(money, period, interest_rate)
