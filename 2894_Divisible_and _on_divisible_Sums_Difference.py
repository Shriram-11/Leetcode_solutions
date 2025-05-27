def difference_of_sums(n, m):
    """
    Calculate the difference between:
    - the sum of all integers from 1 to n that are **not divisible** by m
    - the sum of all integers from 1 to n that **are divisible** by m

    Args:
    n (int): The upper limit of the range (inclusive)
    m (int): The divisor to check divisibility

    Returns:
    int: The result of (sum of non-divisible numbers - sum of divisible numbers)

    Time Complexity: O(n) – we iterate through the range 1 to n once
    Space Complexity: O(1) – constant space usage
    """

    sum_non_divisible = 0  # Sum of numbers not divisible by m
    sum_divisible = 0      # Sum of numbers divisible by m

    for number in range(1, n + 1):
        if number % m == 0:
            sum_divisible += number
        else:
            sum_non_divisible += number

    return sum_non_divisible - sum_divisible
