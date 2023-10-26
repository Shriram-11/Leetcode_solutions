# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # Check if the tree is empty, return an empty list if so
        if not root:
            return []

        # Initialize a queue with the root element
        q = [root]

        # List to store the right side view of the binary tree
        r = []

        # Continue the loop until the queue is empty
        while q:
            # Append the value of the rightmost element in the current level
            r.append(q[-1].val)

            # Initialize a new queue for the next level
            nq = []

            # Iterate through the nodes in the current level
            for n in q:
                # Add the left child to the new queue if it exists
                if n.left:
                    nq.append(n.left)
                
                # Add the right child to the new queue if it exists
                if n.right:
                    nq.append(n.right)

            # Update the current queue to the new queue for the next level
            q = nq

        # Return the list representing the right side view of the binary tree
        return r
