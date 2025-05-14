def lengthAfterTransformations(s, t, nums):
	"""
	:type s: str
	:type t: int
	:type nums: List[int]
	:rtype: int
	"""
	MOD = 10**9 + 7
	
	# If t is 0, return the initial length
	if t == 0:
		return len(s) % MOD
	
	# For t=1, calculate the length directly
	if t == 1:
		length = 0
		for char in s:
			length = (length + nums[ord(char) - ord('a')]) % MOD
		return length
	
	# For t>1, we need to use matrix exponentiation to efficiently compute
	# the length after t transformations
	
	# First build the transformation matrix
	# matrix[i][j] = how many characters of type j are produced by one character of type i
	matrix = [[0] * 26 for _ in range(26)]
	
	for i in range(26):  # For each character 'a' to 'z'
		count = nums[i]
		for j in range(count):
			next_char = (i + j + 1) % 26  # Next character after transformation
			matrix[i][next_char] += 1
	
	# Calculate matrix^(t-1)
	result_matrix = self.matrix_power(matrix, t - 1, MOD)
	
	# Calculate the final length
	length = 0
	for char in s:
		char_index = ord(char) - ord('a')
		for j in range(26):
			length = (length + result_matrix[char_index][j] * nums[j]) % MOD
	
	return length

def matrix_multiply(self, A, B, MOD):
	n = len(A)
	result = [[0] * n for _ in range(n)]
	
	for i in range(n):
		for j in range(n):
			for k in range(n):
				result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % MOD
	
	return result

def matrix_power(self, matrix, power, MOD):
	n = len(matrix)
	result = [[0] * n for _ in range(n)]
	
	# Initialize result as identity matrix
	for i in range(n):
		result[i][i] = 1
	
	# Binary exponentiation
	while power > 0:
		if power & 1:  # If power is odd
			result = self.matrix_multiply(result, matrix, MOD)
		matrix = self.matrix_multiply(matrix, matrix, MOD)
		power >>= 1
	
	return result
