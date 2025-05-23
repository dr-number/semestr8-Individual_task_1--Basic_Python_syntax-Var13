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

def get_text_color(text: str, color: str) -> str:
    return f'{color}{text}{_COLOR_ENDC}'

def is_number(s: str) -> bool:
    try:
        float(s)
        return True
    except ValueError:
        return False

def input_number(text: str, default_value: float = None, min: float = None, max: float = None) -> float:
    while True:
        number = input(f'{get_text_color(text, COLOR_WARNING)} ')
        if number == '' and default_value is not None:
            return default_value
        elif is_number(number):
            num = float(number)
            if min is not None and num < min:
                print(get_text_color(f"Число должно быть не меньше {min}!", COLOR_FAIL))
            elif max is not None and num > max:
                print(get_text_color(f"Число должно быть не больше {max}!", COLOR_FAIL))
            else:
                return num
        else:
            print(get_text_color("Пожалуйста, введите число!", COLOR_FAIL))

def input_integer(text: str, min: int = None, max: int = None) -> int:
    while True:
        num = input_number(text, min=min, max=max)
        if num.is_integer():
            return int(num)
        print(get_text_color("Пожалуйста, введите целое число!", COLOR_FAIL))

def _init_ex_1():
    print('           | ∜(t - s),    если t >= s, 2 < s <= 4,')
    print('f(t, s) = <  s^4 + 2t,    если t < 0,')
    print('           | t + 2        в остальных случаях\n')
    
    t = input_number(text="Введите значение \"t\": ", min=MIN_VALUE, max=MAX_VALUE)
    s = input_number(text="Введите значение \"s\": ", min=MIN_VALUE, max=MAX_VALUE)
    
    result = _ex1(t, s)
    print(f"\nРезультат выполнения функции: {get_text_color(result, COLOR_GREEN)}")

def _ex1(t: float, s: float) -> float:
    if t >= s and 2 < s <= 4:
        print(get_text_color(f'Условие: t >= s и 2 < s <= 4 ({t} >= {s} и 2 < {s} <= 4)', COLOR_WARNING))
        return (t - s) ** (1/4)
    elif t < 0:
        print(get_text_color(f'Условие: t < 0 ({t} < 0)', COLOR_WARNING))
        return s**4 + 2*t
    else:
        print(get_text_color('Условие: иначе', COLOR_WARNING))
        return t + 2

def _init_ex_2():
    print('Вычисление значения функции S')
    print(get_text_color('S = √(1/((lg(cot(x)))^2 - (3x)^(1/4)/cos(x) + sqrt(1/(2x) + 1)) * e^(-3x) + e^(arctg(x))', COLOR_WARNING))
    print('Необходимо проверить принадлежность x области определения функции\n')
    
    while True:
        x = input_number(text="Введите x (в радианах, x > 0, x ≠ πn): ", min=0.0001)
        
        try:
            result = _ex2(x)
            print(f"\nРезультат вычисления функции: {get_text_color(result, COLOR_GREEN)}")
            break
        except ValueError as e:
            print(get_text_color(f"Ошибка: {str(e)}", COLOR_FAIL))
            print(get_text_color("Пожалуйста, введите другое значение x", COLOR_WARNING))

def _ex2(x: float) -> float:
    if math.sin(x) == 0:
        raise ValueError("x не может быть кратным π (sin(x) = 0)")
    
    cot_x = math.cos(x) / math.sin(x)
    if cot_x <= 0:
        raise ValueError("cot(x) должен быть положительным для логарифма")
    
    lg_cot_x = math.log10(cot_x)
    denominator = lg_cot_x**2 - (3*x)**(1/4)/math.cos(x)
    
    if denominator <= 0:
        raise ValueError("выражение под корнем должно быть положительным")
    
    if 2*x == 0:
        raise ValueError("деление на ноль в выражении 1/(2x)")
    
    sqrt_part = math.sqrt(1 / denominator + math.sqrt(1/(2*x) + 1))
    exp_part = math.exp(-3*x) + math.exp(math.atan(x))
    return sqrt_part * exp_part

def _init_ex_3():
    value = input_integer(text="Введите натуральное трехзначное число: ", min=100, max=999)
    result = _ex3(value)
    print(f"\nРезультат выполнения функции: {get_text_color(result, COLOR_GREEN)}")

def _ex3(value: int) -> int:
    digits = str(value)
    
    if len(set(digits)) == 3:
        print(get_text_color("Все цифры уникальны", COLOR_WARNING))
        return value
    elif len(set(digits)) == 1:
        print(get_text_color("Все цифры одинаковы", COLOR_WARNING))
        first = str(int(digits[0]) - 1)
        last = str(int(digits[-1]) + 1) if digits[-1] != '9' else digits[-1]
        return int(first + digits[1:-1] + last)
    else:
        print(get_text_color("Две цифры одинаковы", COLOR_WARNING))
        return int(digits[::-1])

def _init_ex_4():
    print(f"Даны натуральное число n и вещественное x. Вычислить сумму n слагаемых {get_text_color('sin(x) + cos sin(x) + sin cos sin(x) + ...', COLOR_WARNING)}")
    n = input_integer(text="Введите натуральное число n: ", min=1)
    x = input_number(text="Введите вещественное число x: ", min=MIN_VALUE, max=MAX_VALUE)
    
    print("\nХод вычислений:")
    result, steps = _ex4(n, x)
    
    print("\nВсе шаги вычислений:")
    for i, step in enumerate(steps, 1):
        print(f"Шаг {i}: {step}")
    
    print(f"\nИтоговый результат вычисления суммы: {get_text_color(result, COLOR_GREEN)}")

def _ex4(n: int, x: float) -> tuple:
    total = 0.0
    current = x
    steps = []
    
    for i in range(1, n+1):
        operation = "sin" if i % 2 == 1 else "cos"
        prev_value = current
        
        if i % 2 == 1:
            current = math.sin(current)
        else:
            current = math.cos(current)
        
        total += current
        steps.append(f"{operation}({prev_value:.4f}) = {current:.4f} | Текущая сумма: {total:.4f}")
    
    return total, steps

def _init_ex_5():
    value = input_integer(text="Введите натуральное число N: ", min=1)
    result = _ex5(value)
    
    if result[0]:
        print(get_text_color(f"Число {value} является {result[1]}-й степенью числа 5", COLOR_GREEN))
    else:
        print(get_text_color(f"Число {value} НЕ является степенью числа 5", COLOR_FAIL))

def _ex5(n: int) -> tuple:
    if n == 1:
        return True, 0
    
    power = 0
    while n % 5 == 0:
        n //= 5
        power += 1
    
    return n == 1, power

def _init_ex_6():
    print('Известно время начала и окончания (например, 6:00 и 24:00) ')
    print('работы некоторого пригородного автобусного маршрута с одним ')
    print('автобусом на линии, а также протяженность маршрута в минутах ')
    print('(в один конец) и время отдыха на конечных остановках. ')
    print('Составить суточное расписание этого маршрута (моментотправления ')
    print('с конечных пунктов) без учета времени на обед и пересменку.\n')
    print('Составление суточного расписания автобусного маршрута')
    
    while True:
        try:
            start_time = input("Введите время начала работы маршрута (например, 6:00): ")
            end_time = input("Введите время окончания работы маршрута (например, 24:00): ")
            
            start = datetime.strptime(start_time, '%H:%M')
            end = datetime.strptime(end_time, '%H:%M')
            if end <= start:
                end += timedelta(days=1)
            break
        except ValueError:
            print(get_text_color("Некорректный формат времени. Используйте ЧЧ:ММ", COLOR_FAIL))
    
    route_duration = input_integer(text="Введите продолжительность маршрута в минутах (в один конец): ", min=1)
    rest_time = input_integer(text="Введите время отдыха на конечных остановках в минутах: ", min=0)
    
    schedule = _ex6(start, end, route_duration, rest_time)
    
    print("\nСуточное расписание:")
    for i, (departure_a, departure_b) in enumerate(schedule, 1):
        print(f"{i}. Отправление из A: {departure_a.strftime('%H:%M')}, Отправление из B: {departure_b.strftime('%H:%M')}")

def _ex6(start: datetime, end: datetime, route_duration: int, rest_time: int) -> list:
    schedule = []
    current_a = start
    
    while current_a < end:
        arrival_b = current_a + timedelta(minutes=route_duration)
        departure_b = arrival_b + timedelta(minutes=rest_time)
        
        if departure_b > end:
            break
        
        schedule.append((current_a, departure_b))
        current_a = departure_b + timedelta(minutes=route_duration + rest_time)
    
    return schedule

def _init_ex_7():
    print('Вычисление значения суммы бесконечного ряда')
    print(get_text_color('f(x) = 1 + (x^2)/2! + (x^4)/4! + ... + (x^(2*n))/(2n)! + ...', COLOR_WARNING))
    print(f'с заданной точностью {get_text_color("E = 10^-6", COLOR_WARNING)}')
    print(f'и значение функции для проверки {get_text_color("chx = (e^x + e^(-x))/2", COLOR_WARNING)}')
    print(f'учесть, что {get_text_color("0.1 ≤ x ≤ 1", COLOR_WARNING)}\n')
    
    x = input_number(text="Введите x (0.1 ≤ x ≤ 1): ", min=0.1, max=1)
    epsilon = 1e-6
    result, terms = _ex7(x, epsilon)
    check = math.cosh(x)
    
    print(f"\nРезультат вычисления ряда: {get_text_color(result, COLOR_GREEN)}")
    print(f"Проверочное значение (ch x): {get_text_color(check, COLOR_OKCYAN)}")
    print(f"Количество учтенных членов ряда: {terms}")
    print(f"Разница: {abs(result - check)}")

def _ex7(x: float, epsilon: float) -> tuple:
    sum_total = 1.0
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
    print('Вычисление значения суммы бесконечного ряда')
    print(get_text_color('f(x) = x - (x^3)/3 + (x^5)/5 - ... + (((-1)^n) * x^(2n+1)/(2n + 1)) + ...', COLOR_WARNING))
    print(f'с заданной точностью {get_text_color("E = 10^-5", COLOR_WARNING)}')
    print(f'и значение функции для проверки {get_text_color("arctg(x)", COLOR_WARNING)}')
    print(f'учесть, что {get_text_color("|x| < 1", COLOR_WARNING)}\n')
    
    x = input_number(text="Введите x (|x| < 1): ", min=-1+1e-9, max=1-1e-9)
    epsilon = 1e-5
    result, terms = _ex8(x, epsilon)
    check = math.atan(x)
    
    print(f"\nРезультат вычисления ряда: {get_text_color(result, COLOR_GREEN)}")
    print(f"Проверочное значение (arctg x): {get_text_color(check, COLOR_OKCYAN)}")
    print(f"Количество учтенных членов ряда: {terms}")
    print(f"Разница: {abs(result - check)}")

def _ex8(x: float, epsilon: float) -> tuple:
    sum_total = x
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
    print('Дано положительное число k.')
    print(f'Для каждого значения {get_text_color("x = 2,3,4,...,8", COLOR_WARNING)} найти такое наименьшее целое n,')
    print(f'при котором {get_text_color("x^n > k", COLOR_WARNING)}\n')
    
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

def main():
    while True:
        print(
            "\nЛарионов гр. 410з. Программирование на языках высокого уровня\n"
            "Индивидуальное задание №1. Базовый синтаксис Python. Вариант 13.\n"
            "Выберите задачу для выполнения:\n"
            f"{_EX_1}. Найти значение функции f(t, s)\n"
            f"{_EX_2}. Вычислить сложную функцию с проверкой области определения\n"
            f"{_EX_3}. Обработка трехзначного числа\n"
            f"{_EX_4}. Сумма ряда sin x + cos sin x + sin cos sin x + ...\n"
            f"{_EX_5}. Проверка, является ли число степенью 5\n"
            f"{_EX_6}. Составление расписания автобусного маршрута\n"
            f"{_EX_7}. Вычисление суммы ряда (1)\n"
            f"{_EX_8}. Вычисление суммы ряда (2)\n"
            f"{_EX_9}. Нахождение минимальных степеней для чисел 2-8\n"
        )
        
        select = str(input_integer("Введите номер задачи (1-9) или 0 для выхода: ", min=0, max=9))
        
        if select == '0':
            break
        elif select in _ARRAY_EX:
            globals()[f'_init_ex_{select}']()
            input("\nНажмите Enter для продолжения...")
        else:
            print(get_text_color("Некорректный ввод. Пожалуйста, введите число от 1 до 9 или 0 для выхода.", COLOR_FAIL))

if __name__ == '__main__':
    main()
