# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def hasCycle(self, head):
	"""
	Determines if a singly-linked list has a cycle.

	A cycle in a linked list occurs when a node's next pointer points to one of the 
	previous nodes in the list, creating a loop. This function detects such a cycle
	by using a set to store visited nodes. As it traverses the list, it checks if a node
	has been seen before. If so, a cycle is present, and the function returns True. 
	If the traversal reaches the end (i.e., `cur` becomes `None`), it means no cycle exists,
	and the function returns False.

	Time Complexity: O(n), where n is the number of nodes in the linked list.
	Space Complexity: O(n) due to the set used for storing visited nodes.

	:param head: ListNode
		The head node of the singly-linked list to be checked for a cycle.

	:return: bool
		- True if a cycle is detected.
		- False if no cycle is found.

	Example:
		Given the following linked list:
		1 -> 2 -> 3 -> 4 -> 5
			 ↑             |
			 ---------------
		This function will return True, as there's a cycle from node 5 back to node 2.
	"""
	visited = set()  # Initialize an empty set to store visited nodes
	cur = head       # Start traversal from the head node
	
	# Traverse through the list
	while cur:
		if cur in visited:  # If the current node has been seen before, cycle exists
			return True
		visited.add(cur)    # Add the current node to the visited set
		cur = cur.next      # Move to the next node
	
	return False  # No cycle found if traversal reaches the end of the list
