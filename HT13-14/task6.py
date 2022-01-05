"""
Створіть клас в якому буде атрибут який буде рахувати кількість створених екземплярів класів.
"""


class Thing(object):
    counter = 0

    def __init__(self):
        Thing.counter += 1


if __name__ == "__main__":
    tris = 5
    for i in range(tris):
        thing = Thing()
    assert tris == thing.counter
