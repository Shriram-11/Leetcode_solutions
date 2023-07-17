def twosum(nums, target):
    # create an empty dictionary to store number:index
    d = {}
    # iterate over each element
    for idx, num in enumerate(nums):
        # check if a number = target-num exists in the dictionary
        if (target-num) in d:
            return [d[target-num], idx]
        # else update/add the number
        d[num] = idx
