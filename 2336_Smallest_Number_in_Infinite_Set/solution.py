import heapq

class SmallestInfiniteSet(object):

    def __init__(self):
        """
        Initializes the set with numbers from 1 to 1000.
        Uses a min-heap (`min_heap`) for efficient retrieval of the smallest number.
        Uses a set (`removed_numbers`) to track numbers that have been removed.
        """
        self.removed_numbers = set()  # Tracks numbers that have been popped
        self.min_heap = [i for i in range(1, 1001)]  # Min-heap with numbers from 1 to 1000

    def popSmallest(self):
        """
        Removes and returns the smallest number from the set.
        If the set is empty, returns -1.

        :rtype: int
        """
        if self.min_heap:
            smallest = heapq.heappop(self.min_heap)  # Get smallest number
            self.removed_numbers.add(smallest)  # Mark as removed
            return smallest
        return -1  # Return -1 if all numbers have been removed

    def addBack(self, num):
        """
        Adds a number back to the set if it was previously removed.
        Ensures no duplicate insertions in the heap.

        :type num: int
        :rtype: None
        """
        if num in self.removed_numbers:  # Only add back if it was removed before
            heapq.heappush(self.min_heap, num)  # Push it back into the heap
            self.removed_numbers.remove(num)  # Remove from the removed list

# Example usage:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
