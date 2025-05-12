def findEvenNumbers(digits):
    """
    Given a list of digits, find all unique 3-digit even numbers that can be formed
    using the digits exactly once per number (no reuse of the same index).

    :param digits: List[int] - List of single-digit integers (0-9)
    :return: List[int] - Sorted list of valid 3-digit even numbers
    """
    res = set()             # To store unique valid numbers
    count = [0] * 10        # Frequency map for digits (0-9)

    # Count the occurrences of each digit
    for d in digits:
        count[d] += 1

    # Try all possible combinations for hundreds, tens, and units place
    for i in range(1, 10):  # Hundreds digit cannot be 0
        if count[i] == 0:
            continue
        count[i] -= 1       # Use one occurrence of digit i

        for j in range(10):  # Tens digit can be 0-9
            if count[j] == 0:
                continue
            count[j] -= 1   # Use one occurrence of digit j

            for k in range(0, 10, 2):  # Units digit must be even
                if count[k] == 0:
                    continue
                # Form the number and add to result
                res.add(i * 100 + j * 10 + k)

            count[j] += 1   # Backtrack: restore count for j

        count[i] += 1       # Backtrack: restore count for i

    return sorted(list(res))


# Time Complexity: O(1)
#  - The loops run over fixed ranges (1–9, 0–9, 0–8), so the total iterations are constant.
# Space Complexity: O(m)
#  - Size of result array
