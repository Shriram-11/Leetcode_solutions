# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def postorderTraversal(root):
    """
    Perform a postorder traversal of a binary tree.

    Postorder traversal is a type of depth-first traversal where the nodes
    are recursively visited in the following order:
    1. Left subtree
    2. Right subtree
    3. Root node

    This method uses a helper function `post` to perform the recursion
    and collect the values of the nodes in postorder.

    :type root: TreeNode
        The root node of the binary tree.
    :rtype: List[int]
        A list of integers representing the values of the nodes in 
        postorder traversal.
    """

    # List to store the result of the traversal
    self.l = []

    def post(node):
        """
        Recursive helper function to perform postorder traversal.

        :type node: TreeNode
            The current node being visited.
        """
        if node is not None:
            # Recursively visit the left subtree
            post(node.left)
            # Recursively visit the right subtree
            post(node.right)
            # Append the value of the current node after visiting subtrees
            self.l.append(node.val)

    # Start the postorder traversal from the root node
    post(root)
    
    # Return the list of values collected in postorder
    return self.l
