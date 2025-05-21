import math
from datetime import datetime, timedelta

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
_EX_7 = '7'
_EX_8 = '8'
_EX_9 = '9'

_ARRAY_EX = [_EX_1, _EX_2, _EX_3, _EX_4, _EX_5, _EX_6, _EX_7, _EX_8, _EX_9]

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

def _init_ex_6():
    print('Составление суточного расписания автобусного маршрута')
    start_time = input('Введите время начала работы маршрута (например, 6:00): ')
    end_time = input('Введите время окончания работы маршрута (например, 24:00): ')
    route_duration = int(input_number(text="Введите продолжительность маршрута в минутах (в один конец): ", min=1))
    rest_time = int(input_number(text="Введите время отдыха на конечных остановках в минутах: ", min=0))
    
    try:
        start = datetime.strptime(start_time, '%H:%M')
        end = datetime.strptime(end_time, '%H:%M')
        if end <= start:
            end += timedelta(days=1)  # Handle overnight schedules
    except ValueError:
        print(get_text_color("Некорректный формат времени. Используйте формат ЧЧ:ММ", COLOR_FAIL))
        return
    
    schedule = _ex6(start, end, route_duration, rest_time)
    print("\nСуточное расписание:")
    for i, (departure_a, departure_b) in enumerate(schedule, 1):
        print(f"{i}. Отправление из A: {departure_a.strftime('%H:%M')}, Отправление из B: {departure_b.strftime('%H:%M')}")

def _ex6(start: datetime, end: datetime, route_duration: int, rest_time: int) -> list:
    schedule = []
    current_a = start
    total_cycle = 2 * route_duration + 2 * rest_time
    
    while current_a < end:
        arrival_b = current_a + timedelta(minutes=route_duration)
        departure_b = arrival_b + timedelta(minutes=rest_time)
        arrival_a = departure_b + timedelta(minutes=route_duration)
        
        if departure_b > end:
            break
            
        schedule.append((current_a, departure_b))
        current_a = arrival_a + timedelta(minutes=rest_time)
    
    return schedule

def _init_ex_7():
    print('Вычислить значение суммы бесконечного ряда')
    print(get_text_color('f(x) = 1 + (x^2)/2! + (x^4)/4! + ... + (x^(2*n))/(2n)! + ...', COLOR_WARNING))
    print(f'с заданой точностью {get_text_color("E = 10^-6", COLOR_WARNING)} и значение функции для проверки')
    print(f'{get_text_color("chx = (e^x + e^(-x))/2", COLOR_WARNING)}, учесть, что {get_text_color("0,1<=x<=1", COLOR_WARNING)}\n')
    x = input_number(text="Введите x (0.1 ≤ x ≤ 1): ", min=0.1, max=1)
    epsilon = 1e-6
    result, terms = _ex7(x, epsilon)
    check = math.cosh(x)
    print(f"\nРезультат вычисления ряда:   {get_text_color(result, COLOR_GREEN)}")
    print(f"Проверочное значение (ch x): {get_text_color(check, COLOR_OKCYAN)}")
    print(f"Количество учтенных членов ряда: {terms}")
    print(f"Разница между результатом и проверочным значением: {abs(result - check)}")

def _ex7(x: float, epsilon: float) -> tuple:
    sum_total = 1.0  # Первый член ряда (n=0)
    term = 1.0
    n = 1
    while True:
        term *= x * x / ((2 * n - 1) * (2 * n))
        if abs(term) < epsilon:
            break
        sum_total += term
        n += 1
    return sum_total, n

def _init_ex_8():
    print('Вычислить значение суммы бесконечного ряда с заданной точностью')
    print(get_text_color('E = 10^(-5) f(x) = x - (x^3)/3 + (x^5)/5 - ... + (((-1)^n) * x^(2n+1)/(2n + 1)) + ...', COLOR_WARNING))
    print(f'и значение функции (для проверки) {get_text_color("f = arctg(x)", COLOR_WARNING)},')
    print(f'учесть, что {get_text_color("x^2 < 1", COLOR_WARNING)}.\n')
    x = input_number(text="Введите x (|x| < 1): ", min=-1+1e-9, max=1-1e-9)
    epsilon = 1e-5
    result, terms = _ex8(x, epsilon)
    check = math.atan(x)
    print(f"\nРезультат вычисления ряда:       {get_text_color(result, COLOR_GREEN)}")
    print(f"Проверочное значение (arctg x):  {get_text_color(check, COLOR_OKCYAN)}")
    print(f"Количество учтенных членов ряда: {terms}")
    print(f"Разница между результатом и проверочным значением: {abs(result - check)}")

def _ex8(x: float, epsilon: float) -> tuple:
    sum_total = x  # Первый член ряда (n=0)
    term = x
    n = 1
    while True:
        term *= -x * x
        new_term = term / (2 * n + 1)
        if abs(new_term) < epsilon:
            break
        sum_total += new_term
        n += 1
    return sum_total, n

def _init_ex_9():
    k = input_number(text="Введите положительное число k: ", min=0.0001)
    results = _ex9(k)
    print("\nРезультаты:")
    for x, n in results.items():
        print(f"Для x = {x}: минимальное n, при котором x^n > {k} = {get_text_color(n, COLOR_GREEN)}")

def _ex9(k: float) -> dict:
    results = {}
    for x in range(2, 9):
        n = 0
        while True:
            if x ** n > k:
                results[x] = n
                break
            n += 1
    return results

def _init_ex_1():
    print('           | ∜(t - s),    если t >= s, 2 < s <= 4,')
    print('f(t, s) = <  s^4 + 2t,    если t < 0,')
    print('           | t + 2        в остальных случаях\n')
    t = input_number(text="Введите значение \"t\": ", min=MIN_VALUE, max=MAX_VALUE)
    s = input_number(text="Введите значение \"s\": ", min=MIN_VALUE, max=MAX_VALUE)
    print(f"\n Результат выполнения функции: {get_text_color(_ex1(t=t, s=s), COLOR_GREEN)}")

def _ex1(t: float, s: float)-> float:
    if t >= s and 2 < s <= 4:
        print('t >= s and 2 < s <= 4')
        print(get_text_color(f'{t} >= {s} and 2 < {s} <= 4', COLOR_WARNING))
        print(get_text_color(f'({t}-{s}) * (1/4)', COLOR_GREEN))
        return (t-s)**(1/4)

    if t < 0:
        print('t < 0')
        print(get_text_color(f'{t} < 0', COLOR_WARNING))
        print(get_text_color(f'{s}**4 + 2*{t}', COLOR_GREEN))
        return s**4 + 2*t
    
    print('Вариант \'иначе\'')
    print(get_text_color(f'{t} + 2', COLOR_GREEN))
    return t + 2

def _init_ex_3():
    value = int(input_number(text="Введите натуральное трехзначное число: ", min=100, max=999))
    print(f"\n Результат выполнения функции: {get_text_color(_ex3(value=value), COLOR_GREEN)}")

def _ex3(value: int)-> int:
    def is_digits_unique(number: int) -> bool:
        str_number = str(number)
        return len(set(str_number)) == len(str_number)

    def is_digits_identical(number: int) -> bool:
        return len(set(str(number))) == 1

    def modify_number(number: int) -> int:
        str_number = str(number)
        first_digit = str(int(str_number[0]) - 1)
        last_digit = str(int(str_number[-1]) + 1) if str_number[-1] != '9' else str_number[-1]
        return int(first_digit + str_number[1:-1] + last_digit)

    def reverse_number(number: int) -> int:
        return int(str(number)[::-1])

    if is_digits_unique(number=value):
        print(get_text_color(f'Все цифры в числе уникальны. Оставляем число без изменений', COLOR_GREEN))
        return value
    elif is_digits_identical(number=value):
        print(get_text_color(f'Все цифры в числе одинаковы. первую уменьшаем на 1 и последнюю если это не 9 увеличиваем на 1', COLOR_GREEN))
        return modify_number(number=value)
    else:
        print(get_text_color(f'Две цифры в числе одинаковы. Получаем число с обратным порядком чисел', COLOR_GREEN))
        return reverse_number(number=value)

def _init_ex_5():
    value = int(input_number(text="Введите число N: ", min=MIN_VALUE, max=MAX_VALUE))
    _ex5(value=value)

def _ex5(value: int):
    def is_power_of_five(n):
        if n <= 0:
            return False, 0
        
        power = 0
        while n % 5 == 0:
            power += 1
            n //= 5
        
        return n == 1, power

    is_power, power = is_power_of_five(n=value)
    if is_power:
        print(get_text_color(f'Число {value} является {power} степенью числа 5', COLOR_GREEN))
    else:
        print(get_text_color(f'Число {value} НЕ является степенью числа 5', COLOR_FAIL))

def main():
    while True:
        print(
            "\nЛарионов гр. 410з. Программирование на языках высокого уровня\n"
            "Индивидуальное задание №1. Базовый синтаксис Python. Вариант 13.\n"
            "Какую задачу выполнить: \n"
            f'''{get_text_color(f'{_EX_1}) ', COLOR_WARNING)}необходимо найти значение функции в зависимости от введенных параметров.\n'''
            # f'''{get_text_color(f'{_EX_2}) ', COLOR_WARNING)}необходимо найти значение функции в зависимости от
            # введенных параметров. Необходимо проверить, принадлежит ли введенный
            # аргумент области определения функции, вывести сообщение, если не
            # принадлежит, а также предложить повторный ввод параметров. Используйте
            # модуль math или cmath.\n'''
            f'''{get_text_color(f'{_EX_3}) ', COLOR_WARNING)}Дано натуральное трехзначное число. Если все цифры в нем 
            различны, оставить заданное число без изменения; если все цифры одинаковы, первую уменьшить на 1, а 
            последнюю, если это не 9, уве личить на 1; если две цифры в числеодинаковы, получить число с обратным 
            порядком цифр.\n'''
            # f"{get_text_color(f'{_EX_4}) ', COLOR_WARNING)}Вычислить значение s\n"
            f'''{get_text_color(f'{_EX_5}) ', COLOR_WARNING)}Дано натуральное число N. Выяснить, является ли оно степенью числа 5\n'''
            f'''{get_text_color(f'{_EX_6}) ', COLOR_WARNING)}Составить суточное расписание автобусного маршрута\n'''
            f'''{get_text_color(f'{_EX_7}) ', COLOR_WARNING)}Вычислить сумму ряда (1)\n'''
            f'''{get_text_color(f'{_EX_8}) ', COLOR_WARNING)}Вычислить сумму ряда (2)\n'''
            f'''{get_text_color(f'{_EX_9}) ', COLOR_WARNING)}Найти минимальные степени для чисел 2-8\n'''
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

        input('Для продолжения нажмите любую клавишу...')

if __name__ == '__main__':
    main()