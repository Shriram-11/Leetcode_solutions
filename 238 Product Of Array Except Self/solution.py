'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.'''


def productExceptSelf(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    ans = [1]*len(nums)
    pre = post = 1
    for i in range(len(nums)):
        # store the product of all previous elements in ans[i]
        ans[i] *= pre
        pre *= nums[i]
    for i in range(len(nums)-1, -1, -1):
        # store the product of all elements that are ahead of the current index
        ans[i] *= post
        post *= nums[i]
    return ans
