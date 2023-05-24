def twosum(nums,target):
    p={}   # a dictionary to store the number and its latest index

    for idx,num in enumerate(nums):
        if (target-num) in p: # if a number exists such that when added to target-num gives the target
            return [p[target-num],idx]
        p[target-num]=idx #else add the number and its index