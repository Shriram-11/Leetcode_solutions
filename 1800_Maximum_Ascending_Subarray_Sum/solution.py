def maxAscendingSum(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Initialize the current sum of the ascending subarray to the first element.
    # Initialize the maximum sum of any ascending subarray encountered so far.
    current_sum = max_sum = nums[0]
    
    # Start iterating from the second element of the array.
    index = 1
    
    while index < len(nums):
        # If the current element is greater than the previous element, it's part of an ascending sequence.
        if nums[index] > nums[index - 1]:
            # Add the current element to the current sum.
            current_sum += nums[index]
        else:
            # If the sequence is no longer ascending, compare the current sum with the maximum sum found so far.
            max_sum = max(current_sum, max_sum)
            # Reset the current sum to the value of the current element (start a new ascending sequence).
            current_sum = nums[index]
        
        # Move to the next element.
        index += 1
    
    # After the loop, compare and return the maximum sum (either the ongoing current sum or the max found before).
    return max(current_sum, max_sum)
