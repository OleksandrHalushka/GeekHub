"""
4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при
створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
"""


class Figure(object):
    def __init__(self, color):
        self.color = color

    def change_color(self, new_color):
        self.color = new_color


class Oval(Figure):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width


class Square(Figure):
    def __init__(self, color, height, width):
        super().__init__(color)
        self.height = height
        self.width = width


if __name__ == '__main__':
    oval = Oval('red', 2, 5)
    oval.change_color('blue')
    print(oval.color)