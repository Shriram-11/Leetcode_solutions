class Solution(object):
    def addBinary(self, a, b):
        """
        Add two binary strings and return their sum as a binary string.

        This function handles the addition of two binary numbers represented as
        strings, correctly managing the carry bit and ensuring the result is 
        also in binary form. The algorithm processes each bit from right to left,
        summing corresponding bits along with any carry from the previous position.

        Args:
        a (str): A binary string.
        b (str): Another binary string.

        Returns:
        str: The sum of the two binary strings as a binary string.

        Time Complexity: O(n), where n is the length of the longer input string.
        Space Complexity: O(n), to store the resulting binary string.

        The use of % 2 and // 2 in binary addition:
        - `% 2` (Modulo Operation): The `%` operator returns the remainder of a division.
          In binary addition, it helps determine the current bit to be appended to the result.
          For example, when adding two binary digits (0 or 1), along with a carry (0 or 1),
          the result can be 0, 1, 2, or 3. Using `total % 2` gives us the least significant bit
          of the sum, which is the bit to be added to the result:
            - 0 % 2 = 0
            - 1 % 2 = 1
            - 2 % 2 = 0
            - 3 % 2 = 1

        - `// 2` (Integer Division): The `//` operator performs integer division, discarding the
          remainder and returning the quotient. In binary addition, it helps manage the carry for
          the next higher bit. For example, when adding binary digits along with a carry, the integer
          division by 2 determines the carry for the next position:
            - 0 // 2 = 0
            - 1 // 2 = 0
            - 2 // 2 = 1
            - 3 // 2 = 1
        """
        # Initialize carry and the result list
        carry = 0
        result = []

        # Pointers for both strings
        i, j = len(a) - 1, len(b) - 1

        # Loop through both strings from the end to the beginning
        while i >= 0 or j >= 0 or carry:
            # Get the current bits and convert them to integers
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Calculate the sum of the bits and the carry
            total = bit_a + bit_b + carry
            result.append(str(total % 2))  # Current bit (remainder of total divided by 2)
            carry = total // 2  # Update carry (integer division of total by 2)

            # Move to the previous bit
            i -= 1
            j -= 1

        # Since we've added bits from the least significant to the most significant,
        # we need to reverse the result to get the correct binary number
        return ''.join(result[::-1])

# Example usage:
# solution = Solution()
# result = solution.addBinary("1101", "1011")
# print(result)  # Output: "11000"
