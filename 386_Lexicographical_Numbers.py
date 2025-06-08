def lexical_order(n):
    """
    Generate numbers from 1 to n in lexicographical (dictionary) order.

    Lexicographical order means sorting numbers as if they were strings,
    e.g., for n = 13 → [1, 10, 11, 12, 13, 2, 3, ..., 9].

    Approach:
    - Perform a depth-first search (DFS) starting from 1 to 9.
    - From each number, recursively explore its children in the form of current * 10 + i (i = 0 to 9).

    Time Complexity: O(n)
        - Each number from 1 to n is visited exactly once.
    Space Complexity: O(n)
        - Result list stores n elements.
        - Call stack depth is at most log(n) in practice, up to O(n) in worst case due to unbalanced recursion.
    
    :param n: int — The upper bound (inclusive)
    :return: List[int] — List of integers from 1 to n in lexicographical order
    """
    result = []

    def dfs(current):
        if current > n:
            return

        # Add the current number to the result list
        result.append(current)

        # Explore the next level by appending digits 0–9 (like DFS on a tree)
        for i in range(10):
            next_number = current * 10 + i
            if next_number > n:
                return
            dfs(next_number)

    # Start DFS from 1 to 9 (0 is not a valid start for lex order)
    for i in range(1, 10):
        dfs(i)

    return result
