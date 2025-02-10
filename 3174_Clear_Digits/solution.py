def clearDigits(s):
    """
    Remove the last non-digit character for each digit encountered in the string.
    
    :param s: The input string
    :return: A new string after processing
    """
    # If the string is empty, return as is
    if not s:
        return s
    
    # Initialize an empty list to hold the result
    res = []
    
    # Iterate through each character in the input string
    for a in s:
        # If the character is a digit, remove the last character from the result if any
        if a.isdigit():
            if res:  # Ensure there's something to remove
                res.pop()  # Remove last character from the result
        else:
            # If the character is not a digit, add it to the result list
            res.append(a)
    
    # Convert the list back to a string and return
    return "".join(res)
