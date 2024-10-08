def searchRange(nums, target):
	"""
	:type nums: List[int]
	:type target: int
	:rtype: List[int]

	This function finds the starting and ending positions 
	of a given target value in a sorted list. If the target is 
	not found, it returns [-1, -1]. The function uses binary 
	search to efficiently locate the first and last occurrences 
	of the target in the list.

	:param nums: A sorted list of integers
	:param target: An integer to search for in the list
	:return: A list containing the starting and ending index 
			 of the target in the list, or [-1, -1] if not found
	"""
	
	if nums == []:  # Handle the case where the list is empty
		return [-1, -1]

	left = 0
	right = len(nums) - 1
	
	def find_first(left, right):
		"""
		This helper function performs binary search to find the 
		first occurrence of the target in the list.

		:param left: The starting index of the search range
		:param right: The ending index of the search range
		:return: The index of the first occurrence of the target, 
				 or -1 if not found
		"""
		f = -1  # Initialize the first index to -1
		while left <= right:
			key = (left + right) // 2  # Calculate the mid index
			if nums[key] == target:
				f = key  # Update first occurrence
				right = key - 1  # Continue searching in the left half
			elif nums[key] > target:
				right = key - 1  # Move left
			else:
				left = key + 1  # Move right
		return f

	def find_last(left, right):
		"""
		This helper function performs binary search to find the 
		last occurrence of the target in the list.

		:param left: The starting index of the search range
		:param right: The ending index of the search range
		:return: The index of the last occurrence of the target, 
				 or -1 if not found
		"""
		l = -1  # Initialize the last index to -1
		while left <= right:
			key = (left + right) // 2  # Calculate the mid index
			if nums[key] == target:
				l = key  # Update last occurrence
				left = key + 1  # Continue searching in the right half
			elif nums[key] > target:
				right = key - 1  # Move left
			else:
				left = key + 1  # Move right
		return l

	f = find_first(left, right)  # Find the first occurrence
	l = find_last(left, right)    # Find the last occurrence
	return [f, l]  # Return the range [first, last]
