def decodeString(s):
    """
    :param s: The encoded string
    :type s: str
    :return: The decoded string
    :rtype: str
    """

    # Initialize an empty stack to keep track of characters and numbers
    stk = []

    # Iterate through each character in the input string
    for a in s:
        if a != ']':
            # If the character is not ']', push it onto the stack
            stk.append(a)
        else:
            # If the character is ']', start decoding the substring

            # Initialize an empty string for the substring
            sub = ''
            # Build the substring by popping characters from the stack until '[' is encountered
            while stk[-1] != '[':
                sub = stk.pop() + sub
            stk.pop()  # Remove the '[' from the stack

            # Initialize an empty string for the count of repetition
            i = ''
            # Build the count by popping digits from the stack
            while stk and stk[-1].isdigit():
                i = stk.pop() + i

            # Append the decoded substring repeated by the count to the stack
            stk.append(sub * int(i))

    # Concatenate the elements in the stack to get the final decoded string
    return ''.join(stk)
