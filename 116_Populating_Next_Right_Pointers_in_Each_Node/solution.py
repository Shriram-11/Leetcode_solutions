"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # If tree is null return it
        if root is None:
            return root
        # store the adress of head node and its left node
        t1 = root
        t2 = root.left
        # while there exists a left node
        while t1.left:
            # the left element of t1 will point to the right element of current node
            t1.left.next = t1.right
            # if a link exists between t1 and its next element
            if t1.next:
                # the right element of t1 will point to the left element of next node
                t1.right.next = t1.next.left
                t1 = t1.next
            else:
                t1 = t2
                t2 = t1.left
        return root
