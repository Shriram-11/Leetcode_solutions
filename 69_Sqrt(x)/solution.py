def mySqrt(x):
	"""
	Calculate the integer square root of a non-negative integer x.
	
	The integer square root of x is defined as the largest integer n 
	such that n * n <= x. This function uses a binary search approach 
	to find the result efficiently.

	:type x: int  # Input: a non-negative integer
	:rtype: int   # Output: the integer square root of x
	"""
	
	# If x is 0, return 0 as the square root
	if x == 0:
		return 0
	
	# Initialize the search range for binary search
	low, high = 1, x
	
	# Perform binary search
	while low <= high:
		mid = (low + high) // 2  # Calculate the midpoint
		sq = mid * mid  # Square of the midpoint
		
		# Check if we found the exact square root
		if sq == x:
			return mid
		
		# If mid squared is less than x, search in the upper half
		elif sq < x:
			low = mid + 1
		
		# If mid squared is greater than x, search in the lower half
		else:
			high = mid - 1
	
	# Return the largest integer whose square is less than or equal to x
	return high
