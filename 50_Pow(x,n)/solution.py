class Solution(object):
    def myPow(self, x, n):
        """
        Calculate x raised to the power of n (x^n).

        :type x: float
        :param x: The base number.
        :type n: int
        :param n: The exponent. Can be positive, negative, or zero.
        :rtype: float
        :return: The result of x raised to the power of n.
        """
        
        def power(x, n):
            """
            Helper function to calculate x^n using recursion.

            :type x: float
            :param x: The base number.
            :type n: int
            :param n: The exponent. Can be positive or negative.
            :rtype: float
            :return: The result of x raised to the power of n.
            """
            # Base case: any number raised to the power of 0 is 1
            if n == 0:
                return 1
            
            # Handle negative exponents by inverting the base and using positive n
            if n < 0:
                x = 1 / x  # Invert the base
                n = -n     # Use the positive value of n
            
            # If n is even, use the property (x^(n/2))^2
            if n % 2 == 0:
                half = power(x, n // 2)  # Calculate x^(n/2) recursively
                return half * half  # Return the square of the half
            
            # If n is odd, use the property x * x^(n-1)
            return x * power(x, n - 1)  # Multiply x with the result of x^(n-1)

        # Call the helper function to calculate the power
        return power(x, n)
