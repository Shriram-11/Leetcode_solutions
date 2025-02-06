class Solution(object):
    def tupleSameProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tot = 0
        valid = dict()  # Dictionary to store the frequency of products of pairs

        # Iterate over all pairs (i, j) where i < j
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                prod = nums[i] * nums[j]  # Calculate the product of the pair (nums[i], nums[j])
                
                # If the product already exists in the dictionary, increment the count
                if prod in valid:
                    valid[prod] += 1
                else:
                    valid[prod] = 1  # Initialize the count for this product

        # Now we need to count valid tuples
        for a in valid.values():
            # Skip if there are fewer than 2 pairs (we need at least two pairs to form a tuple)
            if a < 2:
                continue
            
            # For each product that has 'a' pairs, calculate the number of ways to pick 2 pairs
            # The number of ways to select 2 pairs from 'a' pairs is given by combination formula: C(a, 2) = a * (a - 1) / 2
            # Multiply by 4 because each pair of pairs can be arranged in 4 distinct ways
            # (abcd), (bacd), (abdc), (badc)
            tot += a * (a - 1) * 4  # This accounts for all valid tuples for this particular product

        return tot
