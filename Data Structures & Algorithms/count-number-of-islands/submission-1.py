class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    #dFS in graph
        if not grid:
            return 0
                
        rows, cols = len(grid), len(grid[0])     
        visited = set()  
        islands = 0

        def dfs(r,c):
            q = deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for x,y in directions:
                    if((row + x) in range(rows) and (col + y) in range(cols) and 
                      grid[row + x][col + y] == "1" and (row + x, col + y) not in visited):
                        q.append((row + x, col + y))
                        visited.add((row + x, col + y))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    islands +=1
        return islands