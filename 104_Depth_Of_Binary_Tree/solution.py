# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # return 0 if tree is empty
        if not root:
            return 0
		# function to get the maximum depth
        def get_height(node,height):
			# return the current depth if we have reached the leaf node
            if not node:
                return height
			# else recursively calulate the depth of left and right sub tree and return the maximum depth
            return max(get_height(node.left,height+1),get_height(node.right,height+1))
        return get_height(root,0)
        
