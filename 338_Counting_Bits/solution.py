def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    #initialize an empty list to store the result
    res=[]
    #iterate from 0 to n+1
    for i in range(n+1):
        #convert i to binary using bin() function
        #count the number of 1's using count()
        #append to result
        res.append(bin(i).count('1'))
    #return the list
    return res
