# Definition for a Node in an N-ary tree.
class Node(object):
    def __init__(self, val=None, children=None):
        """
        Initialize a node in an N-ary tree.

        :param val: The value of the node. Default is None.
        :param children: A list of child nodes. Default is None.
        """
        self.val = val
        self.children = children if children is not None else []

    def postorder(self, root):
        """
        Perform a postorder traversal of an N-ary tree.

        Postorder traversal means visiting all children of a node before visiting the node itself.

        :param root: The root node of the N-ary tree.
        :type root: Node
        :rtype: List[int]
        :return: A list of integers representing the values of the nodes in postorder traversal.
        """
        # List to store the result of postorder traversal
        self.l = []
        
        def post(node):
            """
            Helper function to recursively perform postorder traversal.

            :param node: The current node to process.
            :type node: Node
            """
            if node is not None:
                # Traverse all children of the current node
                for child in node.children:
                    post(child)
                # Append the value of the current node after processing its children
                self.l.append(node.val)
        
        # Start the postorder traversal from the root node
        post(root)
        return self.l
