# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(curr, path):
            """
            Performs a depth-first search (DFS) traversal of the binary tree to calculate the sum of root-to-leaf numbers.
            
            Parameters:
                curr (TreeNode): The current node being processed.
                    - Represents the current node in the traversal.
                    - Type: TreeNode object.
                path (int): The accumulated path sum from the root to the current node.
                    - Represents the sum of numbers formed along the path from the root to the current node.
                    - Type: integer.
            
            Returns:
                int: The total sum of all root-to-leaf numbers.
                    - Represents the sum of all numbers formed from root to leaf nodes in the binary tree.
                    - Type: integer.
            """
            # If the current node is None, return 0.
            if not curr:
                return 0
            
            # Update the path sum by appending the current node's value.
            path = path * 10 + curr.val

            # If the current node is a leaf node, return the accumulated path sum.
            if curr.left is None and curr.right is None:
                return path
            
            # Recursively calculate the sum for left and right subtrees.
            lpath = dfs(curr.left, path)
            rpath = dfs(curr.right, path)
            
            # Return the sum of the path sums from the left and right subtrees.
            return lpath + rpath
        
        # Start the DFS traversal from the root node with an initial path sum of 0.
        return dfs(root, 0)
