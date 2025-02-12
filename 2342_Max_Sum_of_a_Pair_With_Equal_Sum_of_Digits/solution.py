import heapq

def maximumSum(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	# Helper function to calculate the sum of digits of a number
	def sum_of_digits(n):
		tot = 0
		while n > 0:
			tot += n % 10
			n = n // 10
		return tot

	# Dictionary to group numbers by their digit sum
	sums = dict()

	# Process each number in the input list
	for num in nums:
		tot = sum_of_digits(num)
		
		if tot in sums:
			# Push number into the heap, maintaining a heap of size 2
			heapq.heappush(sums[tot], num)
			
			# Ensure only the two largest numbers remain in the heap
			if len(sums[tot]) > 2:
				heapq.heappop(sums[tot])  # Pop the smallest to keep only the largest two
		else:
			sums[tot] = [num]

	max_sum = -float('inf')

	# Iterate over the groups and calculate the maximum sum of valid pairs
	for pairs in sums.values():
		if len(pairs) == 2:
			# If exactly two numbers, take their sum
			max_sum = max(pairs[0] + pairs[1], max_sum)
		elif len(pairs) > 2:
			# If more than two numbers, we already have the two largest in the heap
			max_sum = max(pairs[0] + pairs[1], max_sum)

	return max_sum if max_sum != -float('inf') else -1
