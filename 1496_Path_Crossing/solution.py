def isPathCrossing(self, path):
    """
    :type path: str
    :rtype: bool
    """
    # Create a set to track the coordinates that have been visited
    visited = set()
    
    # Create a dictionary to map each direction to its corresponding coordinate change
    # "N" (North) increases the y-coordinate by 1
    # "S" (South) decreases the y-coordinate by 1
    # "E" (East) increases the x-coordinate by 1
    # "W" (West) decreases the x-coordinate by 1
    d = {"N": (0, 1), "S": (0, -1), "E": (1, 0), "W": (-1, 0)}
    
    # Add the starting position (0, 0) to the set of visited coordinates
    visited.add((0, 0))
    
    # Initialize the current position coordinates
    x, y = 0, 0
    
    # Traverse each direction in the path string
    for a in path:
        # Update the current position based on the direction
        x += d[a][0]
        y += d[a][1]
        
        # Check if the new position has already been visited
        if (x, y) in visited:
            return True  # If visited, the path crosses itself
        
        # Add the new position to the set of visited coordinates
        visited.add((x, y))
    
    # If no crossing is detected, return False
    return False
