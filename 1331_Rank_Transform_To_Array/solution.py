def arrayRankTransform(arr):
	"""
	Transforms the given array into its rank representation.
	
	Each unique number in the array is assigned a rank based on its value,
	with the smallest number getting a rank of 1. Ranks are assigned in 
	ascending order. If multiple occurrences of the same number exist, 
	they all receive the same rank.
	
	Example:
	Input: arr = [40, 10, 20, 10]
	Output: [3, 1, 2, 1]
	
	:type arr: List[int]  # Input list of integers
	:rtype: List[int]     # Output list of integers representing ranks
	"""
	d = dict()  # Dictionary to hold the mapping of each unique number to its rank
	a = sorted(set(arr))  # Create a sorted list of unique numbers from the input array
	rank = 1  # Initialize rank starting from 1
	
	# Assign ranks to each unique number
	for n in a:
		d[n] = rank  # Map the unique number to its corresponding rank
		rank += 1    # Increment rank for the next unique number
	
	# Replace each number in the original array with its corresponding rank
	for i in range(len(arr)):
		arr[i] = d[arr[i]]  # Update the original array with ranks
	
	return arr  # Return the transformed array with ranks
