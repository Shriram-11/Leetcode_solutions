class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeZeroSumSublists(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Convert linked list to list
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
        
        # Find and remove zero sum sublists
        while True:
            found_zero_sum = False
            for i in range(len(lst)):
                prefix_sum = 0
                for j in range(i, len(lst)):
                    prefix_sum += lst[j]
                    if prefix_sum == 0:
                        lst = lst[:i] + lst[j+1:]
                        found_zero_sum = True
                        break
                if found_zero_sum:
                    break
            if not found_zero_sum:
                break
        
        # Reconstruct linked list from modified list
        dummy = ListNode(0)
        current = dummy
        for val in lst:
            current.next = ListNode(val)
            current = current.next
        
        return dummy.next
