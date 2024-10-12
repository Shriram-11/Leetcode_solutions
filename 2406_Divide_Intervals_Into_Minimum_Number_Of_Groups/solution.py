import heapq

def minGroups(self, intervals):
	"""
	:type intervals: List[List[int]]
	:rtype: int
	"""
	# Step 1: Sort intervals by their starting point.
	intervals.sort()
	
	# Step 2: Initialize a min-heap to track the end times of the intervals.
	q = []
	
	# Step 3: Iterate through each interval
	for a in intervals:
		# If the heap is not empty and the current interval starts after the earliest ending interval,
		# it means we can safely merge this interval into the existing group represented by the top of the heap.
		if q and q[0] < a[0]:
			heapq.heappop(q)  # Remove the end time of the finished group

		# Step 4: Add the current interval's end time to the heap.
		# This represents creating a new group or extending an existing group with the current interval.
		heapq.heappush(q, a[1])
	
	# Step 5: The size of the heap represents the number of overlapping groups needed.
	return len(q) if len(q) != 0 else 1
