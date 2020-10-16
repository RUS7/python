'''1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
 принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
 с первым элементом первой строки второй матрицы и т.д.'''

import random


class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        matrix1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

        for i in range(len(self.list1)):

            for j in range(len(self.list2[i])):
                matrix1[i][j] = self.list1[i][j] + self.list2[i][j]

        return str('\n'.join(['\t'.join([str(j) for j in i]) for i in matrix1]))


    def __str__(self):
        return str('\n'.join(['\t'.join()]))



matrix = Matrix([[7, 9, 6], [-5, 22, 1], [1, 0, 3]], [[5, 3, -2], [55, 4, 0], [9, 47, 19]])

print(matrix.__add__())
