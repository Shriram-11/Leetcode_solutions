def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Initialize result to 0, which will hold the final result
    result = 0
    
    # Iterate through each number in the nums list
    for a in nums:
        # Apply XOR between result and the current number
        result ^= a
    
    # Return the result which will be the number that appears only once
    return result

"""
Explanation:

- XOR (^) is a bitwise operation that operates on the binary representations of numbers.
- The XOR operation has the following important properties:
  1. `a ^ a = 0`: XOR of a number with itself results in 0.
  2. `a ^ 0 = a`: XOR of a number with 0 results in the number itself.
  3. XOR is both commutative and associative, meaning the order of operations doesn't matter.

- How XOR helps in finding the single number:
  - Given an array where every number except one appears twice, the numbers that appear twice will cancel each other out when XOR is applied.
  - For example, if the array is [2, 3, 2], the XOR operation would proceed as follows:
    - `result = 0 ^ 2 = 2`
    - `result = 2 ^ 3 = 1`
    - `result = 1 ^ 2 = 3`
  - The final value of `result` will be the number that appears only once, which in this case is 3.
  - This works because the XOR operation will cancel out all pairs of duplicate numbers, leaving only the unique number.

- The algorithm runs in O(n) time complexity and uses O(1) extra space, making it both time-efficient and space-efficient.
"""
