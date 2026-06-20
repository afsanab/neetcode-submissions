class Solution:
    def numIslands(self, grid: List[List[str]]):
        islands = 0
        visited = set()
        def dfs(i,j):
            #base case - out of bounds - "0" - visited alr
            if (i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or
                grid[i][j] == "0" or (i,j) in visited):
                return
            # we are at an unvisited "1"
            # we find all coordinates in the same island by recursing in all 4 dir
            # mark this node visited
            visited.add((i,j))
            dfs(i, j + 1)
            dfs(i, j - 1) 
            dfs(i + 1, j)
            dfs(i - 1, j)
        #call dfs at every unvisited 1, which is a new island to search
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands += 1
                    dfs(row,col)
        return islands