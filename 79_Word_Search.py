def word_exists(board, word):
    """
    Determines if the given word exists in the board by performing a DFS
    from every cell that matches the first character of the word.

    :param board: List[List[str]] - 2D grid of characters
    :param word: str - Word to search for
    :return: bool - True if the word exists in the board, False otherwise
    """

    def dfs(row, col, rows, cols, visited, word_index):
        # Base case: if we've matched all characters in the word
        if word_index == len(word):
            return True

        # 4 possible directions: down, right, up, left
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited.add((row, col))  # Mark current cell as visited

        for dr, dc in directions:
            next_row, next_col = row + dr, col + dc

            # Check boundaries and whether the cell is unvisited and matches the next character
            if (0 <= next_row < rows and 0 <= next_col < cols and
                (next_row, next_col) not in visited and
                board[next_row][next_col] == word[word_index]):
                if dfs(next_row, next_col, rows, cols, visited, word_index + 1):
                    return True

        visited.remove((row, col))  # Backtrack
        return False

    rows, cols = len(board), len(board[0])

    for i in range(rows):
        for j in range(cols):
            # Start DFS only if the cell matches the first character of the word
            if board[i][j] == word[0]:
                if dfs(i, j, rows, cols, set(), 1):  # Start from word[1] since word[0] already matched
                    return True

    return False
