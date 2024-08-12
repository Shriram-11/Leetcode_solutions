class KthLargest(object):
    def __init__(self, k, nums):
        """
        Initializes the KthLargest object with the integer k and the initial stream of integers nums.
        
        :param k: The rank of the largest element to find in the stream.
        :type k: int
        :param nums: The initial list of integers in the stream.
        :type nums: List[int]
        """
        self.k = k  # Store the rank of the largest element to find
        self.nums = nums  # Store the initial list of integers

    def add(self, val):
        """
        Appends the integer val to the stream and returns the kth largest element in the stream.
        
        :param val: The integer to add to the stream.
        :type val: int
        :return: The kth largest element in the stream after adding val.
        :rtype: int
        """
        # Append the new value to the list of integers
        self.nums.append(val)
        
        # Sort the list in descending order
        self.nums.sort(reverse=True)
        
        # Return the kth largest element (which is at index k-1 after sorting)
        return self.nums[self.k - 1]
