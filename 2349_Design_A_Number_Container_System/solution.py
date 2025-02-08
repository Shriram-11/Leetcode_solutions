import heapq

class NumberContainers(object):
    """
    A class that manages a collection of numbers indexed by an integer index.
    Allows for efficient changes to the number associated with an index, as well as
    finding the smallest index associated with a particular number.
    """
    
    def __init__(self):
        """
        Initializes the NumberContainers object.
        
        Initializes two dictionaries:
        - `indexes`: Maps an index to a number.
        - `nums`: Maps a number to a min-heap of indices that are associated with this number.
        """
        self.indexes = dict()  # Maps index -> number
        self.nums = dict()     # Maps number -> min heap of indices

    def change(self, index, number):
        """
        Changes the number associated with a given index.
        
        If the index is already associated with a number, the old number is removed.
        The new index-number association is added, and the index is inserted into
        the min-heap for the given number.
        
        :param index: The index to update.
        :param number: The new number to associate with the index.
        :rtype: None
        """
        # Update the index to number mapping
        self.indexes[index] = number
        
        # If the number is not already in the map, initialize its heap
        if number not in self.nums:
            self.nums[number] = []
        
        # Add the index to the heap for the given number
        heapq.heappush(self.nums[number], index)

    def find(self, number):
        """
        Finds the smallest index that is associated with the given number.
        
        The method pops indices from the heap for the given number and checks if the
        index still maps to the correct number. If an invalid index is encountered (i.e.,
        one that doesn't match the target number), it is discarded. The first valid index 
        is returned. If no valid index is found, returns -1.
        
        :param number: The number to find the smallest index for.
        :rtype: int
        """
        # If the number is not present in the nums dictionary, return -1
        if number not in self.nums:
            return -1
        
        # Process the heap associated with the number
        while self.nums[number]:
            idx = self.nums[number][0]  # Get the smallest index in the heap
            
            # Check if the index is still valid (i.e., maps to the correct number)
            if idx in self.indexes and self.indexes[idx] == number:
                return idx  # Return the valid index
            
            # If the index is stale (no longer maps to the number), pop it from the heap
            heapq.heappop(self.nums[number])
        
        # If no valid index is found, return -1
        return -1


# Example usage:
# obj = NumberContainers()
# obj.change(index, number)    # Changes the number at the given index
# param_2 = obj.find(number)   # Finds and returns the smallest index associated with the number
