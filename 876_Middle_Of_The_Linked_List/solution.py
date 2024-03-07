# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head):
        # Initialize two pointers, slow and fast, both pointing to the head of the list
        slow = fast = head
        
        # Traverse the list with fast pointer moving twice as fast as the slow pointer
        # When fast reaches the end of the list, slow will be at the middle
        while fast and fast.next:
            fast = fast.next.next  # Move fast pointer two steps
            slow = slow.next       # Move slow pointer one step
        
        # Return the node where slow pointer is currently pointing
        return slow
