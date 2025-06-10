from collections import Counter

def max_difference_between_odd_and_even_freq(s):
    """
    Computes the maximum difference between the frequency of two characters in a string,
    where one character has an odd frequency and the other has an even frequency.

    The function looks for:
        max(freq(a1) - freq(a2))
        where:
            - freq(a1) is odd
            - freq(a2) is even

    Parameters:
    ----------
    s : str
        Input string consisting only of lowercase English letters.

    Returns:
    -------
    int
        The maximum difference between an odd frequency and an even frequency character.

    Time Complexity:
    ---------------
    O(n), where n is the length of the input string.
    - Character counting takes O(n).
    - Processing up to 26 distinct letters takes constant time (O(1)).

    Space Complexity:
    ----------------
    O(1)
    - Uses a fixed amount of space for storing character counts (up to 26 lowercase letters).
    """

    # Count frequencies of each character in the string
    counts = Counter(s)

    # Separate frequencies into odd and even
    odd = []
    even = []
    for freq in counts.values():
        if freq % 2 == 0:
            even.append(freq)
        else:
            odd.append(freq)

    # Calculate maximum difference between any odd and any even frequency
    max_diff = float('-inf')
    for o in odd:
        for e in even:
            max_diff = max(max_diff, o - e)

    return max_diff
