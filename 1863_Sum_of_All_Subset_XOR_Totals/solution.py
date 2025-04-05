class Solution(object):
    def subsetXORSum(self, nums):
        """
        Given a list of integers `nums`, this function computes the XOR sum of all subsets.
        
        The XOR sum is defined as the XOR of all elements in each subset, and then the 
        XOR sum of all these subset XORs is returned.

        :type nums: List[int]
        :rtype: int
        """
        
        # Initialize the total XOR sum to 0
        self.total_xor_sum = 0
        
        # Helper function to generate all subsets and calculate their XOR sum
        def generate_subsets(current_subset, index, num_elements):
            """
            Recursively generates all subsets of the list `nums` starting from index `index`, 
            calculates the XOR sum for each subset, and accumulates the result in `self.total_xor_sum`.

            :param current_subset: List representing the current subset being built.
            :param index: Current index being considered in `nums`.
            :param num_elements: Length of the `nums` list.
            """
            # Base case: If all elements have been considered (index == num_elements), calculate XOR for this subset
            if index == num_elements:
                xor_result = 0  # Initialize XOR result for the current subset
                
                # XOR all elements in the current subset `current_subset`
                for num in current_subset:
                    xor_result ^= num
                
                # Add the XOR result of this subset to the total XOR sum
                self.total_xor_sum += xor_result
                return

            # Recursive step: Include the current element nums[index] in the subset
            current_subset.append(nums[index])
            # Recurse by including nums[index] in the subset
            generate_subsets(current_subset, index + 1, num_elements)
            
            # Backtrack: Exclude nums[index] from the subset
            current_subset.pop()
            # Recurse by excluding nums[index] from the subset
            generate_subsets(current_subset, index + 1, num_elements)
        
        # Start recursion with an empty subset and the first index (0)
        generate_subsets([], 0, len(nums))
        
        # Return the total XOR sum of all subsets
        return self.total_xor_sum
