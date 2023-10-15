'''26. Remove Duplicates from Sorted Array
Easy
11K
14.8K
Companies
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.'''


def remove_dup(arr):
    # we need to count the number of duplicate elements as well as first elements in the array must be the unique elements
    s, c = set(), 0
    for i in range(len(arr)):
        if arr[i] not in s:
            arr[c] = arr[i]
            c += 1
            s.add(arr[i])
    return c
