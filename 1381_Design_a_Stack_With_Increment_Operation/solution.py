class CustomStack(object):

    def __init__(self, maxSize):
        """
        Initializes a new instance of CustomStack with a maximum size.

        :param maxSize: int - The maximum number of elements that can be held in the stack.
        """
        self.stk = []  # List to store stack elements
        self.size = 0  # Current size of the stack
        self.m = maxSize  # Maximum size of the stack

    def push(self, x):
        """
        Pushes an integer x onto the stack if the stack has not reached its maximum size.

        :param x: int - The integer to be pushed onto the stack.
        :rtype: None
        """
        if self.size == self.m:  # Check if the stack is full
            return  # Do nothing if full
        self.stk.append(x)  # Add x to the stack
        self.size += 1  # Increment the size of the stack

    def pop(self):
        """
        Removes and returns the top element of the stack. If the stack is empty, returns -1.

        :rtype: int - The top element of the stack or -1 if the stack is empty.
        """
        if self.size == 0:  # Check if the stack is empty
            return -1  # Return -1 if empty
        self.size -= 1  # Decrement the size of the stack
        return self.stk.pop(-1)  # Remove and return the top element

    def increment(self, k, val):
        """
        Increments the bottom k elements of the stack by a given value.

        :param k: int - The number of bottom elements to increment.
        :param val: int - The value to add to each of the bottom k elements.
        :rtype: None
        """
        for i in range(min(k, self.size)):  # Loop through the bottom k elements or the current size
            self.stk[i] += val  # Increment each of the selected elements by val


# Usage example:
# obj = CustomStack(maxSize)
# obj.push(x)       # Push an integer onto the stack
# param_2 = obj.pop()  # Pop the top element from the stack
# obj.increment(k, val)  # Increment the bottom k elements by val
