def scoreOfString(s):
	"""
	Calculate the score of a string based on the absolute differences
	between the ASCII values of consecutive characters.

	:param s: The input string for which the score is to be calculated.
	:type s: str
	:return: The computed score as an integer.
	:rtype: int
	"""
	sc = 0  # Initialize the score to 0
	
	# Iterate through the string, stopping at the second-to-last character
	for i in range(len(s) - 1):
		# Calculate the absolute difference between ASCII values of consecutive characters
		sc += abs(ord(s[i]) - ord(s[i + 1]))
	
	return sc  # Return the final score
