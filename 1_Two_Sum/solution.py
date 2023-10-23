def TwoSum(nums,target):
    #initialize an empty dictionary with number as key and its index as value
    d={}
    #traverse over the array
    for n in range(len(nums)):
        #if a no exits which is exactly equal to target-current_num we found the answer
        if target-nums[n] in d:
            return [d[target-nums[n]],n]
        #else add current number to the list
        d[nums[n]]=n
