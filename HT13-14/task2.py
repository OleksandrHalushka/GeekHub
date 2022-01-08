"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в
відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person(object):

    def __init__(self, name, age, **kwargs):
        self.age = age
        self.name = name
        self.__dict__.update(kwargs)

    def show_age(self):
        return self.age

    def print_name(self):
        return self.name

    def show_all_information(self):
        information = []
        for atr in self.__dict__:
            information.append(f'{atr}: {self.__dict__[atr]}')
        return information


if __name__ == "__main__":
    first_person = Person('Dmytro', 45, profession='banker')
    print(first_person.show_age())
    first_person.print_name()
    print(*first_person.show_all_information())
    second_person = Person('Ivan', 54, surname='Ivanov', profession='seller')
    print(second_person.show_age())
    second_person.print_name()
    print(*second_person.show_all_information())
