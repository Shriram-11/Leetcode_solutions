def three_consecutive_odds(arr):
    """
    Returns True if there are three consecutive odd numbers in the list.

    :param arr: List[int] - input list of integers
    :return: bool - True if any three consecutive numbers are odd, else False

    Time Complexity: O(n) - where n is the length of the input list.
    Space Complexity: O(1) - uses constant extra space.
    """
    consecutive_odds = 0

    for num in arr:
        # Check if current number is odd
        if num % 2 == 1:
            consecutive_odds += 1
            # If we have found 3 in a row, return True early
            if consecutive_odds == 3:
                return True
        else:
            # Reset counter if number is even
            consecutive_odds = 0

    # No three consecutive odds found
    return False
