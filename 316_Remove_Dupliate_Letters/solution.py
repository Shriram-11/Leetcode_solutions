def removeDuplicateLetters(s):
	"""
	Remove duplicate letters from the string `s` such that each letter 
	appears once and only once, and the result is the smallest 
	lexicographical order among all possible results.

	:param s: Input string consisting of lowercase letters
	:type s: str
	:return: A string with unique letters in smallest lexicographical order
	:rtype: str
	"""
	
	# Dictionary to store the last occurrence index of each character
	last_occurrence = {s[i]: i for i in range(len(s))}
	
	# Stack to build the result
	stk = []
	
	# Set to track characters currently in the stack
	in_stack = set()
	
	# Iterate through each character in the input string
	for i in range(len(s)):
		# Skip if the character is already in the stack
		if s[i] in in_stack:
			continue
		
		# Maintain the order in the stack
		while stk and s[i] < stk[-1] and i < last_occurrence[stk[-1]]:
			# If the current character is smaller and the top of the stack
			# will appear later, pop the stack
			in_stack.remove(stk.pop())
		
		# Add the current character to the stack and the set
		stk.append(s[i])
		in_stack.add(s[i])
	
	# Join the stack to form the final result string
	return "".join(stk)
