
def areAlmostEqual(s1, s2):
	"""
	Determine if two strings are almost equal, meaning they can be made equal
	by performing exactly one swap of two characters in one of the strings.

	:type s1: str
	:type s2: str
	:rtype: bool
	"""
	# Step 1: Check if the lengths of both strings are the same
	# If lengths are not the same, they can't be made equal by any swap
	n1, n2 = len(s1), len(s2)
	if n1 != n2:
		return False
	
	# Step 2: Track the indices where characters in the two strings differ
	swap = []
	for i in range(n1):
		if s1[i] != s2[i]:
			swap.append(i)

	# Step 3: Check if there are no mismatches (strings are already equal)
	# If no mismatches, they are already equal and no swap is needed
	if swap == []:
		return True

	# Step 4: If exactly two mismatches, check if swapping those two can make the strings equal
	if len(swap) == 2:
		i, j = swap[0], swap[1]
		# Check if swapping s1[i] with s1[j] makes the strings equal
		return s1[i] == s2[j] and s1[j] == s2[i]
	
	# Step 5: If there are more than two mismatches, it's not possible to make the strings equal with one swap
	return False
