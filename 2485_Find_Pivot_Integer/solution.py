class Solution(object):
    def pivotInteger(self, n):
        """
        Find the pivot integer in a sequence of integers such that the sum of 
        integers to its left is equal to the sum of integers to its right.

        Args:
            n (int): The length of the sequence of integers.

        Returns:
            int: The pivot integer if found, otherwise -1.
        """
        # If the sequence has only one integer, it's considered as the pivot integer
        if n == 1:
            return 1
        
        # Calculate the total sum of integers from 1 to n
        total_sum = (n * (n + 1)) // 2

        # Initialize left and right pointers for binary search
        left = 1
        right = n
        
        # Perform binary search
        while left <= right:
            # Calculate the midpoint
            mid = (left + right) // 2
            # Calculate the sum of integers to the left of mid
            left_sum = (mid * (mid + 1)) // 2

            # Check if the sum to the left of mid is equal to the sum to the right
            # of mid including mid itself
            if left_sum == total_sum - left_sum + mid:
                # If equal, mid is the pivot integer
                return mid
            elif left_sum < total_sum - left_sum + mid:
                # If left sum is less than the right sum, move left pointer to mid + 1
                left = mid + 1
            else:
                # If left sum is greater than the right sum, move right pointer to mid - 1
                right = mid - 1

        # If no pivot integer is found, return -1
        return -1
