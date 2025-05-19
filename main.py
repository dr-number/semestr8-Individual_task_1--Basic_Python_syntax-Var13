import math

COLOR_GREEN = '\033[92m'
COLOR_OKCYAN = '\033[96m'
COLOR_OKBLUE = '\033[94m'
COLOR_WARNING = '\033[93m'
COLOR_FAIL = '\033[91m'
_COLOR_ENDC = '\033[0m'

def get_text_color(text: str, color: str)-> str:
    return f'{color}{text}{_COLOR_ENDC}'


def _ex1(t: float, s: float)-> float:
    if t >= s and 2 < s <= 4:
        return math.sqrt(t-s, 4)

    if t < 0:
        return s**4 + 2*t
    
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
            getattr(_ARRAY_EX[select], 'init')()
        elif select == '0':
            break
        else:
            print(
                f'{get_text_color("Введен неверный номер задачи!", COLOR_FAIL)}'
            )

if __name__ == '__main__':
    main()