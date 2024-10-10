
def maxWidthRamp(self, nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	# Initialize a stack to store indices
	stk = [0]  # Start with the first index
	ramp = 0   # Variable to track the maximum ramp width

	# First pass: Populate the stack with indices
	for i in range(1, len(nums)):
		# Only push the index if it points to a value
		# that is greater than the value at the last index in the stack
		if nums[stk[-1]] > nums[i]:
			stk.append(i)

	# Second pass: Calculate the maximum ramp width
	for i in range(len(nums) - 1, -1, -1):
		# While there are indices in the stack and the value at nums[j]
		# is greater than or equal to the value at the index from the stack
		while stk and nums[stk[-1]] <= nums[i]:
			# Calculate the width of the ramp and update the maximum width
			ramp = max(ramp, i - stk.pop())
	
	return ramp  # Return the maximum ramp width found
