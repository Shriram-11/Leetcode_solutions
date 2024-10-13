def rotate(self, matrix):
	"""
	Rotates the given n x n 2D matrix by 90 degrees clockwise in-place.

	:param matrix: List[List[int]], a square matrix to be rotated.
	:rtype: None, modifies the matrix in-place instead of returning a new one.
	"""
	n = len(matrix)  # Get the size of the matrix

	# Step 1: Transpose the matrix
	for i in range(n):
		for j in range(i + 1, n):  # Start from i + 1 to avoid swapping back
			# Swap the elements at (i, j) and (j, i)
			matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

	# Step 2: Reverse each row to complete the rotation
	for i in range(n):
		matrix[i] = matrix[i][::-1]  # Reverse the current row
