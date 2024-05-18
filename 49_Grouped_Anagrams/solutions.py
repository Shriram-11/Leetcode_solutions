class Solution(object):
    def groupAnagrams(self, strs):
        """
        Groups anagrams together in a list of strings.

        :param strs: List[str]
            List of strings containing words or phrases.
        :return: List[List[str]]
            List of lists where each inner list contains anagrams of each other.

        Example:
        Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
        Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        """

        # Initialize an empty list to store the grouped anagrams
        l = []
        
        # Initialize an index for tracking unique anagram patterns
        i = 0
        
        # Initialize an empty dictionary to store anagram patterns as keys and their corresponding index as values
        d = dict()
        
        # Iterate through each string in the input list
        for a in strs:
            # Sort the characters of the string to create a unique representation of its letters
            # This ensures that anagrams will have the same representation
            n = str(sorted(a))
            
            # If the sorted representation of the string is not already in the dictionary
            if n not in d:
                # Assign the current index to this anagram pattern
                d[n] = i
                
                # Increment the index for the next unique anagram pattern
                i += 1
                
                # Append a new list with the current string to the list of grouped anagrams
                l.append([a])
            else:
                # If the sorted representation of the string is already in the dictionary,
                # append the current string to the list of anagrams with the same pattern
                l[d[n]].append(a)
        
        # Return the list of grouped anagrams
        return l
