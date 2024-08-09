def numMagicSquaresInside(self, grid):
  """
  :type grid: List[List[int]]
  :rtype: int
  """
  def is_magic(i, j):
      """
      This function checks if the 3x3 subgrid starting at (i, j) is a magic square.
      A 3x3 magic square contains numbers 1-9, and each row, column, and diagonal 
      sums to the same target value.
      """
      nums = set()  # Set to store the numbers in the 3x3 subgrid and check for duplicates

      # Check each number in the 3x3 subgrid
      for x in range(3):
          for y in range(3):
              num = grid[i + x][j + y]  # Access the number in the subgrid
              # Check if the number is out of the 1-9 range or if it is a duplicate
              if num < 1 or num > 9 or num in nums:
                  return False  # Not a magic square if any number is out of range or duplicated
              nums.add(num)  # Add the number to the set of seen numbers
      
      # Calculate the target sum using the first row of the 3x3 subgrid
      target = sum(grid[i][j:j+3])
      
      # Check if all rows sum to the target
      for x in range(3):
          r = 0
          for y in range(3):
              r += grid[i + x][j + y]  # Sum up the elements in the row
          if target != r:
              return False  # Not a magic square if any row sum does not match the target
      
      # Check if all columns sum to the target
      for x in range(3):
          c = 0
          for y in range(3):
              c += grid[i + y][j + x]  # Sum up the elements in the column
          if target != c:
              return False  # Not a magic square if any column sum does not match the target
      
      # Check if the main diagonal (top-left to bottom-right) sums to the target
      d1 = 0
      for x in range(3):
          d1 += grid[i + x][j + x]
      if d1 != target:
          return False  # Not a magic square if the main diagonal sum does not match the target
      
      # Check if the anti-diagonal (top-right to bottom-left) sums to the target
      d2 = 0
      for x in range(3):
          d2 += grid[i + x][j + 2 - x]
      if d2 != target:
          return False  # Not a magic square if the anti-diagonal sum does not match the target
      
      return True  # If all checks pass, the subgrid is a magic square
  
  # Dimensions of the grid
  r, c = len(grid), len(grid[0])
  count = 0  # Counter to keep track of the number of magic squares found
  
  # Iterate through the grid, checking every possible 3x3 subgrid
  for i in range(r - 2):
      for j in range(c - 2):
          if is_magic(i, j):
              count += 1  # Increment the counter if a magic square is found
  
  return count  # Return the total count of magic squares
