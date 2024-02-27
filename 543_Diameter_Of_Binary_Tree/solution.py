# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        Calculate the diameter of a binary tree.

        :type root: TreeNode
        :rtype: int
        """
        # Initialize the diameter variable to store the maximum diameter
        self.diameter = 0
        
        def max_depth(node):
            """
            Recursively calculates the maximum depth of a binary tree.

            :param node: Current node being processed.
            :return: Maximum depth of the subtree rooted at the given node.
            """
            # Base case: if the node is None, return 0
            if node is None:
                return 0
            
            # Recursively calculate the maximum depth of the left and right subtrees
            left_depth = max_depth(node.left)
            right_depth = max_depth(node.right)
            
            # Update diameter if the sum of depths of left and right subtrees is greater than current diameter
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the maximum depth of the current subtree rooted at 'node'
            return max(left_depth, right_depth) + 1
        
        # Call the max_depth function to calculate the maximum depth of the tree
        max_depth(root)
        
        # Return the diameter of the binary tree
        return self.diameter
