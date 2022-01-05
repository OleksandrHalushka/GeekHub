"""
Створіть за допомогою класів та продемонструйте свою реалізацію шкільної бібліотеки(включіть фантазію).
"""

class Book(object):

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f'{self.name} by {self.author}'

    def __repr__(self):
        return f'{self.name} by {self.author}'


class Pupil(object):
    debt = []

    def __init__(self, name, surname, group):
        self.name = name
        self.surname = surname
        self.group = group

    def show_debt(self):
        return self.debt

    def __str__(self):
        return f'{self.name} {self.surname} from {self.group} group'

    def __repr__(self):
        return f'{self.name} {self.surname} from {self.group} group'

    def add_to_debt(self, book: Book):
        self.debt.append(book)

    def return_book(self, book: Book):
        self.debt.remove(book)


class Library(object):
    books_in = {}
    pupils = []

    def add_books(self, book: Book, amount):
        if amount > 0:
            if book in self.books_in:
                self.books_in[book] += 1
            else:
                self.books_in.update({book: amount})
        else:
            print('We can`t add amount less then 1')

    def registrate_pupil(self, pupil: Pupil):
        if pupil in self.pupils:
            print(f'Pupil {pupil} is already registered')
        else:
            self.pupils.append(pupil)
            print('Success')

    def take_book(self, pupil, book):
        if book in self.books_in and self.books_in[book] >= 1:
            if pupil in self.pupils:
                if book not in pupil.debt:
                    self.books_in[book] -= 1
                    pupil.add_to_debt(book)
                    print('Success')
                else:
                    print(f'{str(book)} is already taken')
            else:
                print('Unknown pupil, please, registrate him in library')
        else:
            print(f'{str(book)} is not found')

    def return_book(self, pupil, book):
        try:
            pupil.return_book(book)
            self.books_in[book] += 1
        except:
            print(f'{str(pupil)} don`t have {str(book)}')


if __name__ == '__main__':
    library = Library()
    first_book = Book('First book', 'First author')
    second_book = Book('Second book', 'Second author')
    pupil = Pupil('Name', 'Surname', 'Group')
    library.take_book(pupil, first_book)
    library.registrate_pupil(pupil)
    print(*library.pupils)
    library.add_books(first_book, 35)
    library.add_books(second_book, 35)
    print(library.books_in)
    library.take_book(pupil, first_book)
    library.take_book(pupil, second_book)
    print(library.books_in)
    print(pupil.debt)
    library.return_book(pupil, first_book)
    print(library.books_in)
    print(pupil.debt)
    library.return_book(pupil, first_book)
    print(library.books_in)
    library.return_book(pupil, second_book)
    print(library.books_in)
    library.return_book(pupil, second_book)
    print(library.books_in)