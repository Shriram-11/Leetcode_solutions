def findKthBit(n, k):
	"""
	This function finds the k-th bit in the string S_n.
	The binary string S_n is generated recursively as follows:
	S1 = "0"
	Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
	Where:
	- Si-1 is the previous string,
	- "1" is concatenated,
	- reverse(invert(Si-1)) is the reverse of Si-1 with all bits flipped.

	:type n: int  # The index n represents the nth binary string S_n
	:type k: int  # The index k represents the position of the bit in the string
	:rtype: str  # The return type is the k-th bit in S_n, either '0' or '1'
	"""

	# Helper function to reverse and invert a given string `s`
	# Invert: Flip each bit (0 -> 1, 1 -> 0)
	# Reverse: Reverse the order of characters in the string
	def rev(s):
		"""
		Reverse and invert the given string `s`.
		:type s: str
		:rtype: str
		"""
		return ''.join('1' if bit == '0' else '0' for bit in s[::-1])
	
	# Recursive helper function to construct S_n
	# This function builds the binary string S_n by recursively
	# constructing S_(n-1), and applying the rules:
	# S_n = S_(n-1) + "1" + reverse(invert(S_(n-1)))
	def help(n):
		"""
		Recursively constructs the binary string S_n.
		:type n: int
		:rtype: str
		"""
		# Base case: S1 = "0"
		if n == 1:
			return "0"
		
		# Recursive case: Get the previous string S_(n-1)
		a = help(n - 1)
		
		# Invert and reverse the previous string
		b = rev(a)
		
		# Combine S_(n-1), "1", and reverse(invert(S_(n-1)))
		return a + "1" + b
	
	# Generate the full string S_n
	s = help(n)
	
	# Return the k-th bit in the string S_n (0-based index, so return s[k-1])
	return s[k - 1]

