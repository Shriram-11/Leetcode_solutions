class Solution(object):
    def isAnagram(self, s, t):
        """
        Check if two strings are anagrams of each other.

        An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
        typically using all the original letters exactly once.

        Parameters:
        s (str): The first string.
        t (str): The second string.

        Returns:
        bool: True if t is an anagram of s, False otherwise.
        """
        # Check if the lengths of the strings are different.
        if len(s) != len(t):
            return False
        
        # If the lengths are the same, check if the sorted versions of the strings are equal.
        # If they are, then t is an anagram of s.
        return True if sorted(s) == sorted(t) else False
