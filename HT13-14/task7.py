"""
Створити пустий клас, який називається Thing. Потім створіть об'єкт example цього класу.
Виведіть типи зазначених об'єктів.
"""


class Thing(object):
    pass


example = Thing()

if __name__ == "__main__":
    print(type(Thing))
    print(type(example))