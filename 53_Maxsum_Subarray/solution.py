def maxSubArray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # initialize maximum sum to first element
    curr = msum = nums[0]
    # iterate from 0 to n-1
    for i in range(len(nums)-1):
        # check if the current sum is greater if we add the next element
        curr = max(curr+nums[i+1], nums[i+1])
        msum = max(curr, msum)
    return msum
