import heapq

def longestDiverseString(a, b, c):
	"""
	Generates the longest string composed of 'a', 'b', and 'c' 
	such that the same letter does not appear more than two times in a row.

	:type a: int  # Number of 'a's to use
	:type b: int  # Number of 'b's to use
	:type c: int  # Number of 'c's to use
	:rtype: str   # The resulting longest diverse string
	"""
	
	# Priority queue to store counts and corresponding characters
	q = []
	
	# Push non-zero counts into the priority queue with negative counts for max-heap behavior
	if a > 0: 
		heapq.heappush(q, (-a, 'a'))
	if b > 0: 
		heapq.heappush(q, (-b, 'b'))
	if c > 0: 
		heapq.heappush(q, (-c, 'c'))
	
	happy = []  # Resultant list to construct the output string
	
	# Build the longest diverse string
	while q:
		count1, char1 = heapq.heappop(q)  # Get the character with the highest remaining count
		
		# Check if the last two characters in 'happy' are the same as char1
		if len(happy) >= 2 and (happy[-1] == happy[-2] == char1):
			# If they are the same, we need to pick a different character
			if not q:  # If no other characters are left, we break out
				break
			count2, char2 = heapq.heappop(q)  # Get the next character
			
			happy.append(char2)  # Append the different character
			count2 += 1  # Decrement the count of that character
			
			if count2:  # If there's still some left, push it back into the queue
				heapq.heappush(q, (count2, char2))
		else:
			# If it's safe to add char1, append it to 'happy'
			happy.append(char1)
			count1 += 1  # Decrement the count of char1
			
		if count1:  # If there's still some 'char1' left, push it back into the queue
			heapq.heappush(q, (count1, char1))
	
	# Join the list into a string and return
	return "".join(happy)
