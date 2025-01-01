# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # If the tree is empty (root is None), return 0 as there's no level to process
        if not root:
            return 0
        
        # If the tree only has one node (root), return that node's value as it's the only level
        if not root.left and not root.right:
            return root.val

        # Initialize the score variable to track the maximum sum encountered
        score = float('-inf')
        # Initialize level variable to track the level number with the maximum sum
        level = 0
        # Initialize current_level counter for keeping track of which level we are processing
        cl = 0
        # Initialize a queue (FIFO) for level-order traversal of the tree
        q = [root]

        # Perform a level-order traversal using a queue
        while q:
            cl += 1  # Increment the level number

            # Get the number of nodes at the current level
            n = len(q)
            # Initialize a variable to store the sum of node values at the current level
            cur_sum = 0

            # Process all nodes at the current level
            for _ in range(n):
                node = q.pop(0)  # Pop the front node from the queue
                cur_sum += node.val  # Add the value of the current node to the current sum

                # If the current node has a left child, add it to the queue
                if node.left:
                    q.append(node.left)
                # If the current node has a right child, add it to the queue
                if node.right:
                    q.append(node.right)

            # After processing all nodes at the current level, check if the current sum is greater
            # than the previous highest sum, and update the score and level if so
            if cur_sum > score:
                score = cur_sum  # Update the maximum sum
                level = cl  # Update the level corresponding to the maximum sum

        # Return the level with the maximum sum of node values
        return level
