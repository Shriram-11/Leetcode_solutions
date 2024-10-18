def isValidSudoku(self, board):
	"""
	Determines if a 9x9 Sudoku board is valid according to the following rules:
	- Each row must contain the digits 1-9 without repetition.
	- Each column must contain the digits 1-9 without repetition.
	- Each of the nine 3x3 sub-boxes must contain the digits 1-9 without repetition.

	Args:
		board (List[List[str]]): A 9x9 2D list representing the Sudoku board.
								  Each cell contains a digit from '1' to '9' or '.' for empty cells.

	Returns:
		bool: True if the board is valid, False otherwise.
	"""

	# Initialize sets to track seen numbers in rows, columns, and 3x3 boxes
	rows = [set() for _ in range(9)]
	cols = [set() for _ in range(9)]
	boxes = [set() for _ in range(9)]

	# Iterate through each cell in the board
	for i in range(9):
		for j in range(9):
			a = board[i][j]
			
			# Skip empty cells
			if a == ".":
				continue
			
			# Check for duplicates in the current row, column, and box
			if (a in rows[i]) or (a in cols[j]) or (a in boxes[(i // 3) * 3 + (j // 3)]):
				return False
			
			# Add the number to the respective row, column, and box sets
			rows[i].add(a)
			cols[j].add(a)
			boxes[(i // 3) * 3 + (j // 3)].add(a)

	# If no duplicates were found, the board is valid
	return True
