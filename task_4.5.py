'''5. Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти
четные числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех
элементов списка.
Подсказка: использовать функцию reduce().
'''

from functools import reduce



def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')

# my_list = [num for num in range(100, 1001)]
# sum_my_list = reduce(lambda x, y: x * y, my_list)
# print(sum_my_list)

print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')