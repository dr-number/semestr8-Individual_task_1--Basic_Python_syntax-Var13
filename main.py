import math

COLOR_GREEN = '\033[92m'
COLOR_OKCYAN = '\033[96m'
COLOR_OKBLUE = '\033[94m'
COLOR_WARNING = '\033[93m'
COLOR_FAIL = '\033[91m'
_COLOR_ENDC = '\033[0m'

MIN_VALUE = -10_000
MAX_VALUE = 10_000

_EX_1 = '1'
_EX_2 = '2'
_EX_3 = '3'
_EX_4 = '4'
_EX_5 = '5'
_EX_6 = '6'

_ARRAY_EX = [_EX_1, _EX_2, _EX_3, _EX_4, _EX_5, _EX_6]

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(str)-> bool:
    try:
        float(str)
        return True
    except ValueError:
        return False

def input_number(text: str, default_value: float = None, min: float = None, max: float = None)-> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '':
            if default_value is not None:
                return default_value
            else:
                print(get_text_color(f"Введите число!", COLOR_FAIL))
        elif is_number(number):
            if min is not None and float(number) < min:
                print(get_text_color(f"Минимально допустимое число - {min}!", COLOR_FAIL))
            elif max is not None and float(number) > max:
                print(get_text_color(f"Максимально допустимое число - {max}!", COLOR_FAIL))
            else:
                return float(number)
        else:
            print(get_text_color(f"\"{number}\" - не число! Повторите ввод!", COLOR_FAIL))
            
    return 0.0


def _init_ex_1():
    t = input_number(text="Введите значение \"t\": ", min=MIN_VALUE, max=MAX_VALUE)
    s = input_number(text="Введите значение \"s\": ", min=MIN_VALUE, max=MAX_VALUE)
    print(f"\n Результат выполнения функции: {get_text_color(_ex1(t=t, s=s), COLOR_GREEN)}")


def _ex1(t: float, s: float)-> float:
    if t >= s and 2 < s <= 4:
        print('t >= s and 2 < s <= 4')
        print(get_text_color(f'{t} >= {s} and 2 < {s} <= 4', COLOR_GREEN))
        return math.sqrt(t-s, 4)

    if t < 0:
        print('t < 0')
        print(f'{t} < 0')
        return s**4 + 2*t
    
    print('Вариант \'иначе\'')
    return t + 2




def main():
    while True:
        print(
            "\nЛарионов гр. 410з. Программирование на языках высокого уровня\n"
            "Индивидуальное задание №1. Базовый синтаксис Python. Вариант 13.\n"
            "Какую задачу выполнить: \n"
            f'''{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}необходимо найти значение функции в зависимости от введенных параметров.\n'''
            f'''{get_text_color(f'{_EX_2}) ', COLOR_WARNING)}необходимо найти значение функции в зависимости от
            введенных параметров. Необходимо проверить, принадлежит ли введенный
            аргумент области определения функции, вывести сообщение, если не
            принадлежит, а также предложить повторный ввод параметров. Используйте
            модуль math или cmath.\n'''
            f"{get_text_color(f'{_EX_3}) ', COLOR_WARNING)}используйте вложенный условный оператор\n"
            f"{get_text_color(f'{_EX_4}) ', COLOR_WARNING)}Вычислить значение s\n"
            f"{get_text_color(f'{_EX_5}) ', COLOR_WARNING)}Определить, лежит ли точка с координатами (x,y) внутри квадрата\n"
            f"{get_text_color(f'{_EX_6}) ', COLOR_WARNING)}По заданному графику функции вычислить ее значение\n"
        )
        select = input('Для выхода введите \'0\'\n')

        if select in _ARRAY_EX:
            globals()[f'_init_ex_{select}']()
        elif select == '0':
            break
        else:
            print(
                f'{get_text_color("Введен неверный номер задачи!", COLOR_FAIL)}'
            )

if __name__ == '__main__':
    main()