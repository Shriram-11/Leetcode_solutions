class Solution(object):
    def isSameTree(self, p, q):
        """
        Determines if two binary trees are identical.

        Args:
        - p (TreeNode): Root of the first binary tree.
        - q (TreeNode): Root of the second binary tree.

        Returns:
        - bool: True if both trees are structurally identical and have the same node values, False otherwise.
        """

        def same_tree(a, b):
            """
            Recursively compares two binary trees.

            Args:
            - a (TreeNode): Root of the first binary tree.
            - b (TreeNode): Root of the second binary tree.

            Returns:
            - bool: True if both trees are structurally identical and have the same node values, False otherwise.
            """
            # If one node is None and the other is not, they can't be the same
            if (a is None and b is not None) or (a is not None and b is None):
                return False
            # If both nodes are None, they are considered the same
            if a is None and b is None:
                return True
            # If the values of the nodes are different, trees are not identical
            if a.val != b.val:
                return False
            # Recursively check left and right subtrees
            return same_tree(a.left, b.left) and same_tree(a.right, b.right)

        return same_tree(p, q)
