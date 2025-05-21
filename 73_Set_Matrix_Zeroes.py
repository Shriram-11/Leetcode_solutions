def set_zeroes(matrix):
    """
    Modifies the input matrix in-place such that if an element is 0, 
    its entire row and column are set to 0.

    :param matrix: List[List[int]] - 2D matrix of integers
    :rtype: None
    """

    # Sets to track which rows and columns need to be zeroed
    zero_rows = set()
    zero_cols = set()

    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # First pass: record the rows and columns that contain a zero
    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 0:
                zero_rows.add(row)
                zero_cols.add(col)

    # Second pass: update the matrix cells to zero based on recorded rows and columns
    for row in range(num_rows):
        for col in range(num_cols):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0

# Time Complexity: O(m * n)
# - m = number of rows
# - n = number of columns
# We traverse the entire matrix twice.

# Space Complexity: O(m + n)
# - We use two sets to store row and column indices that need to be zeroed.
