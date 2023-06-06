class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        # sort the array to get the sequence in a proper order
        arr.sort()
        # find common diffrence
        d = arr[1] - arr[0]
        # iterate from 1 to length -1
        for i in range(len(arr) - 1):
            # if the difference between two consecutive elements is not same as the common difference its not an Arithematic Progressions
            if arr[i + 1] - arr[i] != d:
                return False
        # return true as all the iterations were True
        return True
