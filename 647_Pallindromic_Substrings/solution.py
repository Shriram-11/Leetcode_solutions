class Solution(object):
    def countSubstrings(self, s):
        """
        Counts the number of palindromic substrings in the given string.

        :param s: str - The input string to check for palindromic substrings.
        :rtype: int - The total count of palindromic substrings.
        """
        self.count = 0  # Initialize count of palindromic substrings
        
        # Function to expand around the center indices and count palindromes
        def expand_around_center(left, right):
            """
            Expands around the given center indices and counts palindromes.

            :param left: int - The left index of the center.
            :param right: int - The right index of the center.
            """
            while left >= 0 and right < len(s) and s[left] == s[right]:
                self.count += 1  # Increment count for each palindrome found
                left -= 1  # Move left index inward
                right += 1  # Move right index outward

        # Iterate through each character in the string
        for i in range(len(s)):
            # Check for odd-length palindromes centered at s[i]
            expand_around_center(i, i)
            # Check for even-length palindromes centered between s[i] and s[i + 1]
            expand_around_center(i, i + 1)

        return self.count  # Return the total count of palindromic substrings
