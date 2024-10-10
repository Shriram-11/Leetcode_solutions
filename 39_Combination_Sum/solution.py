class Solution(object):
    def combinationSum(self, candidates, target):
        """
        Given a list of candidates and a target value, this function finds all unique combinations 
        of candidates where the chosen numbers sum to the target. The same number can be chosen 
        multiple times in the combination.

        :type candidates: List[int]  # A list of integers representing candidate numbers.
        :type target: int  # An integer representing the target sum.
        :rtype: List[List[int]]  # A list of lists, where each sublist represents a valid combination of candidate numbers summing to the target.

        This function uses a recursive backtracking approach to explore all possible combinations.

        Example:
        Input: candidates = [2,3,6,7], target = 7
        Output: [[2, 2, 3], [7]]
        """
        
        self.combs = []  # List to store the valid combinations.
        
        def help(total, n, idx, temp):
            """
            Helper function that performs the backtracking to find valid combinations.

            :type total: int  # The current sum of the numbers in the temporary list.
            :type n: int  # The total number of candidates.
            :type idx: int  # The current index of the candidate being considered.
            :type temp: List[int]  # The temporary list storing the current combination.

            This function explores two possibilities at each recursive call:
            1. Including the candidate at the current index (allowing repetitions).
            2. Excluding the candidate at the current index and moving on to the next one.
            """
            # If the current sum matches the target, add the current combination to the result.
            if total == target:
                self.combs.append(temp[:])
                return
            
            # If the total exceeds the target or we have considered all candidates, return.
            if total > target or idx == n:
                return
            
            # Include the candidate at the current index and explore further.
            temp.append(candidates[idx])
            help(total + candidates[idx], n, idx, temp)
            
            # Backtrack by removing the last candidate.
            temp.pop()
            
            # Explore the option of excluding the candidate and moving to the next one.
            help(total, n, idx + 1, temp)
        
        # Start the recursion with an initial total of 0 and an empty temporary list.
        help(0, len(candidates), 0, [])
        
        return self.combs  # Return the list of valid combinations.
