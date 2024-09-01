def construct2DArray(original, m, n):
	"""
	:type original: List[int]
	:type m: int
	:type n: int
	:rtype: List[List[int]]
	"""
	# Check if it's possible to form a 2D array with dimensions m x n from the original list
	if m * n != len(original):
		return []  # If not possible, return an empty list

	l = []  # Initialize an empty list to store the resulting 2D array

	# Iterate over the original list in steps of n to construct each row of the 2D array
	for i in range(0, len(original), n):
		l.append(original[i:i + n])  # Slice the original list to create a row and add it to the result list

	return l  # Return the 2D array constructed from the original list
