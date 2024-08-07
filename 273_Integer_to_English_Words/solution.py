def numberToWords(num):
    """
    :type num: int
    :rtype: str
    """
    # Handle the special case where the input number is zero
    if num == 0:
        return "Zero"

    # Helper function to convert single digit numbers (1-9) to words
    def ones(n):
        return ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][n]
    
    # Helper function to convert numbers between 10 and 19 to words
    def teens(n):
        return ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"][n % 10]
    
    # Helper function to convert multiples of ten (20, 30, ..., 90) to words and handle the numbers in between
    def tens(n):
        return ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"][n // 10] + ("" if n % 10 == 0 else " " + ones(n % 10))
    
    # Helper function to convert numbers less than 100 to words
    def two_digits(n):
        if n == 0:
            return ""
        if n < 10:
            return ones(n)
        if n < 20:
            return teens(n)
        else:
            return tens(n)
    
    # Helper function to convert numbers less than 1000 to words
    def three_digits(n):
        if n < 100:
            return two_digits(n)
        return ones(n // 100) + " Hundred" + ("" if n % 100 == 0 else " " + two_digits(n % 100))    
    
    # List to accumulate parts of the final result
    res = []
    
    # Dictionary to map units to their names
    d = {1000000000: "Billion", 1000000: "Million", 1000: "Thousand"}
    
    # Loop through each unit (billion, million, thousand) and process the corresponding part of the number
    for unit in [1000000000, 1000000, 1000]:
        if num >= unit:
            res.append(three_digits(num // unit) + " " + d[unit])
            num = num % unit
    
    # Process the remainder of the number (less than 1000)
    if num > 0:
        res.append(three_digits(num))
    
    # Join the parts together with spaces and return the final result
    return ' '.join(res)
