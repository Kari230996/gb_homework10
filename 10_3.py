'''Третье задание'''


class Cell:
    def __init__(self, cell):
        self.cell = cell

    def __add__(self, other):
        return f'Сложение двух клеток: {self.cell + other.cell}'

    def __sub__(self, other):
        result = self.cell - other.cell
        if result < 0:
            return 'Операцию невозможно проводить'
        else:
            return f'Разность ячеек двух клеток: {result}'

    def __mul__(self, other):
        return f'Произведение двух клеток: {self.cell * other.cell}'

    def __floordiv__(self, other):
        return f'Целочисленное деление двух клеток: {self.cell // other.cell}'

    def make_order(self, rows):

        return '\n'.join(['*' * rows for i in range(self.cell // rows)]) + '\n' + '*' * (self.cell % rows)

cell = Cell(24)
cell1 = Cell(12)
print(cell + cell1)
print(cell - cell1)
print(cell * cell1)
print(cell // cell1)
print(cell.make_order(7))
