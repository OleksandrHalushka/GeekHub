"""
Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
"""

from time import sleep


class TimeError(Exception):
    pass

# Використав трішки інше розуміння світлофора - доки для авто жовтий - для пішоходів червоний
# Функція дозволяє налаштувати інтервал зеленого, червоного (жовтий завжди дві секунди)
# Залежнно від update=True чи update=False функція друкує результат в ону строку чи послідовно
#


def traffic_lights(green_time=5, red_time=3, update=True):
    if green_time <= 0 or red_time <= 0:
        raise TimeError('Minimal time is 1 second')
    relations = {
        'Red': 'Green',
        'Yellow': 'Red',
        'Green': 'Red'
    }
    cycle = []
    for times in range(green_time):
        cycle.append('Green')
    for times in range(2):
        cycle.append('Yellow')
    for times in range(red_time):
        cycle.append('Red')
    while True:
        for colour in cycle:
            if update:
                print('\r', f'{colour}'.ljust(10), f'{relations[colour]}'.rjust(10), end='')
            else:
                print(f'{colour}'.ljust(10), f'{relations[colour]}'.rjust(10))
            sleep(1)


if __name__ == '__main__':
    green = int(input('Please, input time for green light for cars in seconds '))
    red = int(input('Please, input time for red light for cars in seconds '))
    lights = traffic_lights(green, red)
    try:
        lights
    except Exception as exp:
        print(exp)
    else:
        lights
