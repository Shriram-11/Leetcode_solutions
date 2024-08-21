from collections import defaultdict

class Solution(object):
    def countWords(self, words1, words2):
        """
        Counts the number of words that appear exactly once in each of the two given lists.

        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        # Initialize a defaultdict to keep track of word counts.
        # Each word will map to a list where:
        # - index 0 represents the count in words1
        # - index 1 represents the count in words2
        count = defaultdict(lambda: [0, 0])
        
        # Count occurrences of each word in words1
        for word in words1:
            count[word][0] += 1
        
        # Count occurrences of each word in words2
        for word in words2:
            count[word][1] += 1
        
        # Initialize a counter for words that appear exactly once in both lists
        c = 0
        
        # Iterate over the items in the count dictionary
        for w, l in count.items():
            # Check if the word appears exactly once in both lists
            if l[0] == 1 and l[1] == 1:
                c += 1  # Increment the counter for valid words
        
        return c  # Return the total count of valid words
