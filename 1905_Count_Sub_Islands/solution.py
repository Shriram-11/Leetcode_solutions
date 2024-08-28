def countSubIslands(grid1, grid2):
    """
    :type grid1: List[List[int]]
    :type grid2: List[List[int]]
    :rtype: int
    """
    from collections import deque
    
    d = [(0,1),(1,0),(-1,0),(0,-1)]
    r, c = len(grid2), len(grid2[0])
    visited = [[False] * c for _ in range(r)]
    count = 0
    
    def bfs(x, y):
        cells = deque([(x, y)])
        visited[x][y] = True
        sub_island = True
        while cells:
            cx, cy = cells.popleft()
            if not (0 <= cx < r and 0 <= cy < c) or not grid2[cx][cy]:
                continue
            if not grid1[cx][cy]:  # If grid1 does not have land where grid2 does
                sub_island = False
            for dx, dy in d:
                nx, ny = cx + dx, cy + dy
                if (0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and grid2[nx][ny]):
                    visited[nx][ny] = True
                    cells.append((nx, ny))
        return sub_island
    
    for x in range(r):
        for y in range(c):
            if not visited[x][y] and grid2[x][y]:
                if bfs(x, y):
                    count += 1
    
    return count
