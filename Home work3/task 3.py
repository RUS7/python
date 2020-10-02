"""3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших
двух аргументов."""


def my_func(numbers):
    sum_2max = sum(numbers) - min(numbers)
    return sum_2max


numbers = [7, 5, 9]
print(my_func(numbers))