"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції
з 2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
"""


class Calc(object):
    """Simple calculator for two numbers and four operations with saving last result in object"""

    def __init__(self):
        self.last_result = None

    @staticmethod
    def _to_float(x, y):
        try:
            x = float(x)
            y = float(y)
            return x, y
        except:
            return

    @staticmethod
    def _to_int(result):
        if result % 1 == 0:
            result = int(result)
        return result

    def add(self, x: float or int, y: float or int):
        """Adds y to x and returns result in integer or float type"""

        if self._to_float(x, y):
            x, y = self._to_float(x, y)
            result = x + y
            self.last_result = self._to_int(result)
            return self.last_result
        else:
            return 'Incorrect type'

    def subtract(self, x: float or int, y: float or int):
        """Subtracts y from x and returns result in integer or float type"""

        if self._to_float(x, y):
            x, y = self._to_float(x, y)
            result = x - y
            self.last_result = self._to_int(result)
            return self.last_result
        else:
            return 'Incorrect type'

    def divide(self, x: float or int, y: float or int):
        """divides x by y and handles division by zero error"""

        if self._to_float(x, y):
            x, y = self._to_float(x, y)
            try:
                result = x / y
            except ZeroDivisionError:
                return 'Division by zero is not possible'
            self.last_result = self._to_int(result)
            return self.last_result
        else:
            return 'Incorrect type'

    def multiply(self, x: float or int, y: float or int):
        """Multiplies x by y returns result in integer or float type"""

        if self._to_float(x, y):
            x, y = self._to_float(x, y)
            result = x * y
            self.last_result = self._to_int(result)
            return self.last_result
        else:
            return 'Incorrect type'


if __name__ == '__main__':
    # тестуємо функції на очікуваний результат
    calc = Calc()
    assert calc.last_result is None
    assert calc.add(1, 2) == 3 and calc.last_result == 3
    assert calc.subtract(2, 1) == 1 and calc.last_result == 1
    assert calc.divide(6, 3) == 2 and calc.last_result == 2
    assert calc.multiply(2, 2) == 4 and calc.last_result == 4
    # тестуємо ділення на 0
    assert calc.divide(6, 0) == 'Division by zero is not possible'
    # тестуємо, що останій результат прив"язано до конкретного екземпляру, а не класу в цілому
    second_calk = Calc()
    assert second_calk.last_result is None
    assert calc.add('kajsdfoi', 45) == "Incorrect type", calc.last_result == 4
    assert calc.add('kajsdfoi', 45) == "Incorrect type", calc.last_result == 4