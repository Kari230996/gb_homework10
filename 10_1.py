'''Первое задание'''


class Matrix:
    def __init__(self, matrix):   # реализуем перегрузку конструктора класса нашей матрицы
        self.matrix = matrix

    def __str__(self):    # реализуем перегрузку метода для вывода матрицы в привычном виде
        return '\n'.join([''.join(['%d\t' % i for i in row]) for
                          row in self.matrix])

    def __add__(self, other):    # реализуем перегрузку метода для сложения двух объектов (двух матриц)
        result = [[self.matrix[i][j] + other.matrix[i][j] for j in range
        (len(self.matrix[0]))] for i in range(len(self.matrix))]

        return '\n'.join([''.join(['%d\t' % i for i in row]) for    # распакуем списки матрицы
                            row in result])


m = Matrix([[31, 22, 6], [37, 34, 23], [51, 86, 33]])
m1 = Matrix([[3, 5, 12], [2, 4, -12], [-1, 64, -7]])

print(str(m))  # правильный вывод матрицы в виде строк
print()
print(str(m1))
print()
print(m + m1) # вывод сложения двух матриц







