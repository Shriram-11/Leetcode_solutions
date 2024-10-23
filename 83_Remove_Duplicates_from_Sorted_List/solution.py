# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def deleteDuplicates(head):
	"""
	Remove duplicates from a sorted linked list.

	:param head: Optional[ListNode] - The head of the sorted linked list.
	:return: Optional[ListNode] - The head of the linked list with duplicates removed.
	"""
	# Initialize a pointer to the current node
	res = head
	
	# Iterate through the linked list until reaching the end
	while res and res.next:
		# If the current node's value is the same as the next node's value
		if res.val == res.next.val:
			# Skip the next node by linking to the node after the next
			res.next = res.next.next
		else:
			# Move to the next node if no duplicate is found
			res = res.next
	
	# Return the modified head of the linked list
	return head
