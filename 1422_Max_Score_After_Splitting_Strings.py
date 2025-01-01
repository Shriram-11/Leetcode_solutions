def maxScore(s):
	"""
	:type s: str
	:rtype: int
	"""
	# Check if the string length is 1, in that case the score is 0
	if len(s) == 1:
		return 0
	
	# Initialize the number of ones at the right end of the string
	ones = 1 if s[-1] == "1" else 0
	
	# Get the length of the string
	n = len(s)
	
	# Start pivoting from the second last character (n-2)
	pivot = n - 2
	
	# Initialize the number of zeroes on the left of the string
	zeroes = 0
	
	# Initialize score with a very low number to ensure we update it properly
	score = float('-inf')
	
	# Count the number of zeroes in the string (left part before pivot)
	for i in range(n - 1):
		if s[i] == "0":
			zeroes += 1
	
	# Traverse the string from the second last character to the first
	while pivot > 0:
		# Update the score by considering the sum of ones on the right and zeroes on the left
		score = max(score, ones + zeroes)
		
		# If the current character is "0", decrease the zero count on the left
		if s[pivot] == "0":
			zeroes -= 1
		else:
			# If it's "1", increase the ones count on the right
			ones += 1
		
		# Move the pivot one step to the left
		pivot -= 1
	
	# Return the maximum score considering the final counts of zeroes and ones
	return max(score, zeroes + ones)
