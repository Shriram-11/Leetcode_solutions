def isHappy(n):
	"""
	Determines if a number n is a happy number.

	A happy number is defined by the process of replacing the number 
	by the sum of the squares of its digits. This process is repeated 
	until the number equals 1 (indicating it is happy) or falls into 
	a cycle that does not include 1 (indicating it is not happy).

	:type n: int: The number to check
	:rtype: bool: True if n is a happy number, False otherwise
	"""
	
	def help(n):
		"""
		Helper function to calculate the sum of the squares of the digits of n.

		:type n: int: The number whose digits are to be squared and summed
		:rtype: int: The sum of the squares of the digits of n
		"""
		ss = 0  # Initialize the sum of squares
		while n != 0:
			d = n % 10  # Get the last digit of n
			ss += (d * d)  # Add the square of the digit to the sum
			n = n // 10  # Remove the last digit from n
		return ss  # Return the sum of squares

	seen = set()  # Set to keep track of numbers we've encountered
	while n != 1 and n not in seen:
		seen.add(n)  # Add the current number to the set of seen numbers
		n = help(n)  # Update n to be the sum of the squares of its digits

	return n == 1  # Return True if n equals 1 (happy number), otherwise False
