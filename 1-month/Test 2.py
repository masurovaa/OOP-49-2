""" Функция 'Калькулятор' """
import math

def func_divide(f_num, s_num):  # divide - разделить
    print(f'Ваш ответ: {f_num / s_num}')


def func_multiply(f_num, s_num):  # multiply - умножить
    print(f'Ваш ответ: {f_num * s_num}')


def func_summ(f_num, s_num):  # summ - сложить
    print(f'Ваш ответ: {f_num + s_num}')


def func_subtract(f_num, s_num):  # subtract - вычесть
    print(f'Ваш ответ: {f_num - s_num}')


def func_degree_num(f_num, degree_1):  # degree_num - степень числа
    print(f'Ваш ответ: {f_num ** degree_1}')


def sqr_root_num(f_num):  # sqr_root_num - квадратный корень числа
    print(f'Ваш ответ: {math.sqrt(f_num)}')


while True:
    command = input('Хотите использовать калькулятор? Выберите команду "да" или "нет": ').lower()
    if command == "нет":
        print("Выход из программы. До свидания!")
        break
    elif command != "да":
        print("Некорректный ввод. Попробуйте снова.")
        continue

    print('''Вас приветствует калькулятор, ниже приведены его функции:
 - Умножить 
 - Разделить 
 - Сложить 
 - Вычесть 
 - Число в степени 
 - Квадратный корень числа''')

    choose = input("Выберите одну из приведённых функций >> ").lower()

    if choose == "разделить":
        f_num = float(input("Введите первое число >> "))
        s_num = float(input("Введите второе число >> "))
        func_divide(f_num, s_num)

    elif choose == "умножить":
        f_num = float(input("Введите первое число >> "))
        s_num = float(input("Введите второе число >> "))
        func_multiply(f_num, s_num)

    elif choose == "сложить":
        f_num = float(input("Введите первое число >> "))
        s_num = float(input("Введите второе число >> "))
        func_summ(f_num, s_num)

    elif choose == "вычесть":
        f_num = float(input("Введите первое число >> "))
        s_num = float(input("Введите второе число >> "))
        func_subtract(f_num, s_num)

    elif choose == "число в степени":
        f_num = float(input("Введите число >> "))
        degree = float(input("Введите степень числа >> "))
        func_degree_num(f_num, degree)

    elif choose == "квадратный корень числа":
        f_num = float(input("Введите число в корне >> "))
        if f_num < 0:
            print("Квадратный корень из отрицательного числа невозможен.")
        else:
            sqr_root_num(f_num)

    else:
        print("< Неизвестный запрос >")