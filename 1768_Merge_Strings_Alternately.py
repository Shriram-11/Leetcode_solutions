def mergeAlternately(word1, word2):
    """
    Merge two strings by alternating their characters.
    If one string is longer, append the remaining characters at the end.

    Args:
        word1 (str): First input string.
        word2 (str): Second input string.

    Returns:
        str: Alternately merged string.
    """
    i = j = 0
    len1, len2 = len(word1), len(word2)
    res = ""

    while i < len1 or j < len2:
        if i < len1:
            res += word1[i]

        if j < len2:
            res += word2[j]

        i += 1
        j += 1

    return res
"""
### Complexity Analysis

* **Time Complexity:** `O((n + m)^2)` in Python because strings are immutable, and each `+=` creates a new string.

  * `n = len(word1)`
  * `m = len(word2)`

* **Space Complexity:** `O(n + m)` for the output string.

> A more efficient Python solution would use a list and `"".join()` to achieve **O(n + m)** time complexity.
"""
