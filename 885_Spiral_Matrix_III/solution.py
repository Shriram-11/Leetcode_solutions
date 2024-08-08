def spiralMatrixIII(rows, cols, rStart, cStart):
    """
    Generates a list of coordinates representing a clockwise spiral traversal
    of a grid starting from the given cell (rStart, cStart).
    
    :type rows: int - Number of rows in the grid
    :type cols: int - Number of columns in the grid
    :type rStart: int - Starting row index
    :type cStart: int - Starting column index
    :rtype: List[List[int]] - List of coordinates visited in spiral order
    """
    # Directions for right, down, left, and up movements
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    
    step = 1  # Number of steps to take in the current direction
    direction = 0  # Index for current direction (0: right, 1: down, 2: left, 3: up)
    visited = []  # List to store visited coordinates
    
    # Continue traversal until all cells are visited
    while len(visited) < rows * cols:
        # Traverse in the current direction for `step` number of times
        for _ in range(2):  # There are two sets of movements for each step size (one horizontal, one vertical)
            for j in range(step):  # Move `step` number of times in the current direction
                # Check if the current position is within grid bounds
                if 0 <= rStart < rows and 0 <= cStart < cols:
                    visited.append([rStart, cStart])  # Add the position to the visited list
                
                # Move to the next cell in the current direction
                rStart += directions[direction][0]
                cStart += directions[direction][1]
            
            # Change direction (clockwise: right -> down -> left -> up)
            direction = (direction + 1) % 4
        
        # Increase step size after completing both horizontal and vertical moves
        step += 1
    
    return visited  # Return the list of visited coordinates in spiral order
