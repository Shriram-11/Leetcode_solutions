class MyCircularDeque(object):
    def __init__(self, k):
        """
        Initializes the deque with a maximum capacity of k.
        
        :param k: int - the maximum number of elements that can be stored in the deque.
        """
        self.k = k
        self.front = 0  # Points to the front element of the deque
        self.rear = 0   # Points to the next position for inserting at the rear
        self.size = 0   # Current number of elements in the deque
        self.q = [0] * k  # List to hold the elements of the deque

    def insertFront(self, value):
        """
        Inserts an element at the front of the deque.
        
        :param value: int - the value to be inserted.
        :rtype: bool - returns True if the operation is successful, False if the deque is full.
        """
        if not self.isFull():
            self.front = (self.front - 1 + self.k) % self.k  # Move front pointer
            self.q[self.front] = value  # Insert the value
            self.size += 1  # Increment the size
            return True
        return False

    def insertLast(self, value):
        """
        Inserts an element at the rear of the deque.
        
        :param value: int - the value to be inserted.
        :rtype: bool - returns True if the operation is successful, False if the deque is full.
        """
        if not self.isFull():
            self.q[self.rear] = value  # Insert the value
            self.rear = (self.rear + 1) % self.k  # Move rear pointer
            self.size += 1  # Increment the size
            return True
        return False
        
    def deleteFront(self):
        """
        Deletes an element from the front of the deque.
        
        :rtype: bool - returns True if the operation is successful, False if the deque is empty.
        """
        if not self.isEmpty():
            self.front = (self.front + 1) % self.k  # Move front pointer
            self.size -= 1  # Decrement the size
            return True
        return False
        
    def deleteLast(self):
        """
        Deletes an element from the rear of the deque.
        
        :rtype: bool - returns True if the operation is successful, False if the deque is empty.
        """
        if not self.isEmpty():
            self.rear = (self.rear - 1 + self.k) % self.k  # Move rear pointer
            self.size -= 1  # Decrement the size
            return True
        return False

    def getFront(self):
        """
        Gets the front element of the deque without removing it.
        
        :rtype: int - returns the front element if the deque is not empty, otherwise returns -1.
        """
        if not self.isEmpty():
            return self.q[self.front]
        return -1

    def getRear(self):
        """
        Gets the rear element of the deque without removing it.
        
        :rtype: int - returns the rear element if the deque is not empty, otherwise returns -1.
        """
        if not self.isEmpty():
            return self.q[self.rear - 1]  # Get the last inserted element
        return -1

    def isEmpty(self):
        """
        Checks whether the deque is empty.
        
        :rtype: bool - returns True if the deque is empty, otherwise returns False.
        """
        return self.size == 0

    def isFull(self):
        """
        Checks whether the deque is full.
        
        :rtype: bool - returns True if the deque is full, otherwise returns False.
        """
        return self.size == self.k

# Usage example:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
