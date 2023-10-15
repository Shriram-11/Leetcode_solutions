'''
There is a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).'''


def arraySign(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    c = 0
    for a in nums:
        # count the no. of negative elements
        if a < 0:
            c += 1
        # if 0 exists in list the product will be 0 hence return 0
        if a == 0:
            return 0
    # if no. of negative elements in even product will be positve else negative
    if c % 2 == 0:
        return 1
    return -1
