"""1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль."""


def my_division(number1, number2):
    try:
        10 / number2
    except ZeroDivisionError:
        print('Деление на ноль!')

    division = number1 / number2
    return division


number1 = int(input('Введите число: '))
number2 = int(input('Введите число: '))

print(my_division(number1, number2))