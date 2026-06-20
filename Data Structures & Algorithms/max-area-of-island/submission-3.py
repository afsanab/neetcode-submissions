class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sizes = []
        visited = set()

        def dfs(grid, r, c, visited):
            # base case: no more neighbors that are valid - return size
            if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or grid[r][c] == 0 or (r,c) in visited:
                return 0
            visited.add((r,c))
            size = 1
            # othewise - recurse - left/right/up/down + add the return value to count
            size += dfs(grid, r - 1, c, visited)
            size += dfs(grid, r + 1, c, visited)
            size += dfs(grid, r, c + 1, visited)
            size += dfs(grid, r, c - 1, visited)
            # return count   
            return size     
        # loop through the grid
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # when we reach a 1 - call dfs to get its full island and return the size
                if grid[row][col] == 1 and (row,col) not in visited: 
                    new_size = dfs(grid, row, col, visited)
                    sizes.append(new_size)
        return max(sizes) if sizes else 0



