import numpy
import copy

class SudokuSolver:
	def __init__(self, grid):
		self.problem_grid = grid
		self.solution_grid = numpy.zeros((9,9))

	
	def __str__(self):
		return f"Le problème est :\n{self.problem_grid}"

	def verify_possible_value(self, index_line, index_column, possible_value):
		"""
		Cette fonction permet de vérifier si la valeur que l'on souhaite rajouter
		respecte bien les règles du jeu Sudoku.
		Elle renvoie True quand la valeur est cohérente.
		Elle renvoie False quand la valeur ne respecte pas les règles.
		"""
		the_value_is_valid = True

		# Vérification sur la ligne
		for idx_col in range(0, 9):
			if possible_value == self.problem_grid[index_line][idx_col]:
				the_value_is_valid = False
		
		# Vérification sur la colonne:
		for idx_line in range(0, 9):
			if possible_value == self.problem_grid[idx_line][index_column]:
				the_value_is_valid = False

		# Vérification sur le bloc de la cellule
		
		# ici on détermine les indexes de début du bloc
		idx_line_starting_bloc = (index_line // 3) * 3
		idx_col_starting_bloc = (index_column // 3) * 3

		#ici on détermine les indexes de fin du bloc
		idx_line_end_bloc = idx_line_starting_bloc + 3
		idx_col_end_bloc = idx_col_starting_bloc + 3

		
		for idx_line in range(idx_line_starting_bloc, idx_line_end_bloc):
			for idx_col in range(idx_col_starting_bloc, idx_col_end_bloc):
				
				if possible_value == self.problem_grid[idx_line][idx_col]:
					
					the_value_is_valid = False

		return the_value_is_valid


	def solve(self):
		if 0 not in self.problem_grid and 0 in self.solution_grid:
			self.solution_grid = copy.copy(self.problem_grid)

		number_lines_of_problem = self.problem_grid.shape[0]
		number_columns_of_problem = self.problem_grid.shape[1]
		
		for index_line in range(0, number_lines_of_problem):
			for index_column in range(0, number_columns_of_problem):
				
				if self.problem_grid[index_line][index_column] == 0:
					for possible_value in range(1, 10):
						if self.verify_possible_value(index_line, index_column, possible_value):
							self.problem_grid[index_line][index_column] = possible_value
							self.solve()
							self.problem_grid[index_line][index_column] = 0

					return None


	def show_solution(self):
		if 0 not in self.solution_grid:
			print(self.solution_grid)
		else:
			self.solve()
			self.show_solution()
