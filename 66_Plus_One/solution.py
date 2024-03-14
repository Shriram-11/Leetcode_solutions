class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # Initialize a variable `n` to store the integer representation of digits
        n = 0
        
        # Loop through each digit in the `digits` array
        for i in digits:
            # Multiply the current value of `n` by 10 and add the current digit
            n = n * 10 + i
        
        # Convert the integer `n` to a string and increment by 1
        n = str(n + 1)
        
        # Convert each character of the resulting string back to an integer
        # and store it in a list, returning the resulting list
        return [int(i) for i in n]
