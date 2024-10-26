def searchMatrix(smatrix, target):
	"""
	Searches for a target value in a 2D matrix.

	:type matrix: List[List[int]]: A 2D list of integers, where each row is sorted in ascending order.
	:type target: int: The integer value to search for.
	:rtype: bool: Returns True if the target is found in the matrix, otherwise False.
	"""
	
	def search(row, v):
		"""
		Performs binary search on a single row to find the target value.

		:type row: List[int]: A list of integers sorted in ascending order.
		:type v: int: The integer value to search for.
		:rtype: bool: Returns True if the value is found, otherwise False.
		"""
		l, r = 0, len(row) - 1  # Initialize left and right pointers.
		while l <= r:
			m = (l + r) // 2  # Calculate the middle index.
			if row[m] == v:  # Target found.
				return True
			elif row[m] < v:  # Target is in the right half.
				l = m + 1
			else:  # Target is in the left half.
				r = m - 1
		return False  # Target not found in the row.

	for r in matrix:
		if r[-1] == target:  # Check if the last element of the row is the target.
			return True
		if r[-1] > target:  # If the last element is greater, search in this row.
			return search(r, target)

	return False  # Target not found in any row.

