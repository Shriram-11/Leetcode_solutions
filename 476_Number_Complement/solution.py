def findComplement(num):
    """
    Find the complement of a given integer.
    
    The complement of a number is obtained by flipping all the bits in its binary representation.
    For example, if the input is 5 (binary: 101), the complement is 2 (binary: 010).

    :type num: int  # The input integer whose complement needs to be found.
    :rtype: int    # Returns the integer value of the complement.
    """
    # Initialize an empty string to build the binary complement representation
    s = ""
    
    # Iterate over the binary representation of 'num', excluding the '0b' prefix
    for a in bin(num)[2:]:
        # Flip the bit: '1' becomes '0', and '0' becomes '1'
        if a == '1':
            s += '0'
        else:
            s += '1'

    # Convert the binary complement string back to an integer and return it
    return int(s, 2)
