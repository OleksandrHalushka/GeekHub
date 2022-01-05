"""
Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і метод
для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для завдання
початкових розмірів об'єктів при їх створенні.
"""


class Figure(object):

    color = 'white'

    def change_color(self, new_color):
        self.color = new_color


class Oval(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width


class Square(Figure):
    def __init__(self, height, width):
        self.height = height
        self.width = width


if __name__ == '__main__':
    figure = Figure()
    print(figure.color)
    figure.change_color('black')
    new_figure = Figure()
    print(figure.color)
    print(new_figure.color)
    oval = Oval(1, 2)
    print(oval.color)
    oval.change_color('black')
    print(oval.color)
