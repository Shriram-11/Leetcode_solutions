def fractionAddition(self, expression):
    """
    Adds fractions given in the form of a string and returns the result in its simplest form.
    
    :type expression: str
    :rtype: str
    """
    
    def gcd(a, b):
        """
        Computes the greatest common divisor (GCD) of two integers using the Euclidean algorithm.
        
        :type a: int
        :type b: int
        :rtype: int
        """
        while b != 0:
            a, b = b, a % b
        return abs(a)
    
    def lcm(a, b):
        """
        Computes the least common multiple (LCM) of two integers using the formula:
        LCM(a, b) = (a * b) // GCD(a, b).
        
        :type a: int
        :type b: int
        :rtype: int
        """
        return (a * b) // gcd(a, b)
    
    def solve(a, b, p, q):
        """
        Adds two fractions with numerators and denominators (a/b) and (p/q), and returns the result as 
        a new numerator and denominator.
        
        :type a: int  # Numerator of the first fraction
        :type b: int  # Denominator of the first fraction
        :type p: int  # Numerator of the second fraction
        :type q: int  # Denominator of the second fraction
        :rtype: tuple[int, int]  # New numerator and denominator after addition
        """
        d = lcm(b, q)  # Find the least common multiple of the denominators
        a = a * (d // b)  # Scale the first fraction's numerator
        p = p * (d // q)  # Scale the second fraction's numerator
        return (a + p), d  # Return the combined numerator and common denominator
    
    def reduce(a, b):
        """
        Reduces the fraction (a/b) to its simplest form by dividing both numerator and denominator by their GCD.
        
        :type a: int  # Numerator
        :type b: int  # Denominator
        :rtype: tuple[int, int]  # Reduced numerator and denominator
        """
        c = gcd(a, b)  # Compute the GCD of the numerator and denominator
        return a // c, b // c  # Return the simplified fraction
    
    # Initialize the result as 0/1 (zero fraction)
    n, d = 0, 1
    
    # Current index in the expression string
    i, l = 0, len(expression)
    
    # Initial sign for fractions
    sign = "+"
    
    while i < l:
        # Handle sign of the fraction
        if expression[i] in "+-":
            sign = expression[i]
            i += 1
        
        # Parse the numerator
        num = 0
        while i < l and expression[i] in "0123456789":
            num = (num * 10) + int(expression[i])
            i += 1
        i += 1  # Move past the '/' character
        
        # Apply sign to the numerator
        if sign == "-":
            num = -num
        
        # Parse the denominator
        den = 0
        while i < l and expression[i] in "0123456789":
            den = (den * 10) + int(expression[i])
            i += 1
        
        # Add the current fraction to the result
        n, d = solve(n, d, num, den)
    
    # Reduce the final result to its simplest form
    n, d = reduce(n, d)
    
    # Return the result as a string in the format "numerator/denominator"
    return str(n) + "/" + str(d)
