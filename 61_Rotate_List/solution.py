# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def rotateRight(head, k):
	"""
	Rotates a singly-linked list to the right by k places.

	:param head: Optional[ListNode] - The head of the linked list to be rotated.
	:param k: int - The number of places to rotate the list to the right.
	:return: Optional[ListNode] - The new head of the rotated linked list.
	"""
	
	# If the list is empty, return None
	if not head:
		return head
	
	cur = head  # Pointer to traverse the list
	l = 1       # Initialize the length of the list

	# Calculate the length of the list and find the last node
	while cur.next:
		l += 1
		cur = cur.next
	
	# Connect the last node to the head to form a circular linked list
	cur.next = head
	
	# Calculate the effective number of rotations needed
	k = l - (k % l)
	
	# Traverse to the node before the new head
	while k > 0:
		cur = cur.next
		k -= 1
	
	# The new head will be the node after cur
	nh = cur.next
	# Break the circular connection
	cur.next = None
	
	return nh
