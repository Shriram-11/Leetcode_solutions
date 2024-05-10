class Solution(object):
    def divide(self, dividend, divisor):
        """
        Divide two integers without using multiplication, division, and mod operator.

        Args:
            dividend (int): The dividend.
            divisor (int): The divisor.

        Returns:
            int: The quotient after dividing dividend by divisor.

        Notes:
            The integer division truncates toward zero, losing its fractional part.
            If the quotient is greater than 2^31 - 1, return 2^31 - 1.
            If the quotient is less than -2^31, return -2^31.

        """

        # Determine the sign of the result
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        
        # Take the absolute values of dividend and divisor
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize the result
        res = 0
        
        # Perform long division algorithm
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1  # Left shift i by 1 (equivalent to multiplying i by 2)
                temp <<= 1  # Left shift temp by 1 (equivalent to multiplying temp by 2)

        # Adjust the sign of the result
        if sign < 0:
            res = -res

        # Ensure the result is within the 32-bit signed integer range
        return min(max(-2147483648, res), 2147483647)
