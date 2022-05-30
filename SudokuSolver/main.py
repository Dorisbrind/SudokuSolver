import numpy
from sudoku_solver import *

grid = numpy.array([[0, 0, 6, 5, 3, 0, 0, 1, 0],
					[0, 0, 0, 0, 2, 0, 5, 0, 4],
					[2, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 8, 0, 3, 4, 2],
					[0, 0, 0, 9, 0, 3, 0, 0, 0],
					[6, 3, 1, 0, 4, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 7],
					[8, 0, 4, 0, 6, 0, 0, 0, 0],
					[0, 6, 0, 0, 7, 1, 8, 0, 0]])


sudoku = SudokuSolver(grid)

print(sudoku)
print("Affichage de la solution")
sudoku.show_solution()

