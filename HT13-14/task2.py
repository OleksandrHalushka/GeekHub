"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в
відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person(object):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def show_age(self):
        try:
            return self.age
        except:
            return 'Age is undefined'

    def print_name(self):
        try:
            print(self.name)
        except:
            print('Name is undefined')
            return 'Name is undefined'

    def show_all_information(self):
        information = []
        for atr in self.__dict__:
            information.append(f'{atr}: {self.__dict__[atr]}')
        return information


if __name__ == "__main__":
    first_person = Person(age=21, name='Dmytro', profession='banker')
    print(first_person.show_age())
    first_person.print_name()
    print(first_person.show_all_information())
    second_person = Person(surname='Ivanov', profession='seller')
    print(second_person.show_age())
    second_person.print_name()
    print(second_person.show_all_information())