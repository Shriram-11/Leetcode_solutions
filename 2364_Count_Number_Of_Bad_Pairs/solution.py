def countBadPairs(nums):
	"""
	:type nums: List[int]
	:rtype: int
	
	This function calculates the number of bad pairs in the given array 'nums'. A pair (i, j) 
	is considered a bad pair if i < j and nums[j] - j != nums[i] - i.

	The idea is to track the difference between the value of an element and its index, i.e., 
	(nums[i] - i). This difference helps in identifying "good pairs". The key observation is:
	- If nums[j] - j == nums[i] - i for j > i, then the pair (i, j) is a good pair.
	- A bad pair is simply one that does not satisfy this condition.

	We maintain a dictionary `diff_count` to track the occurrences of each difference 
	(nums[i] - i). For each index, we check how many times the same difference has appeared 
	before, which gives us the number of good pairs with that index.

	The total number of pairs is then the difference between all pairs and the good pairs.
	"""
	# Dictionary to store the frequency of each difference (nums[i] - i)
	diff_count = dict()
	# Variable to keep track of the total number of bad pairs
	bad_pairs = 0
	
	for i in range(len(nums)):
		# Calculate the difference (nums[i] - i)
		diff = i - nums[i]
		
		# If the difference has appeared before, retrieve the number of good pairs
		if diff in diff_count:
			good_pairs = diff_count[diff]
		else:
			good_pairs = 0
		
		# The bad pairs are calculated by subtracting the number of good pairs 
		# (with the current index i) from i. This is because if the same difference
		# has occurred `good_pairs` times before, then `i - good_pairs` will give 
		# us the number of bad pairs.
		bad_pairs += (i - good_pairs)
		
		# Update the frequency of the current difference
		diff_count[diff] = good_pairs + 1

	# Return the total number of bad pairs
	return bad_pairs
