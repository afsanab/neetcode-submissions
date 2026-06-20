class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        sizes = []
        visited = set()

        def dfs(grid, r, c, visited):
            # base case
            if (r < 0 or c < 0 or 
                r == len(grid) or c == len(grid[0]) or 
                grid[r][c] == 0 or 
                (r, c) in visited):
                return 0

            visited.add((r, c))
            size = 1

            size += dfs(grid, r - 1, c, visited)
            size += dfs(grid, r + 1, c, visited)
            size += dfs(grid, r, c + 1, visited)
            size += dfs(grid, r, c - 1, visited)

            return size

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1 and (row, col) not in visited:
                    new_size = dfs(grid, row, col, visited)
                    sizes.append(new_size)

        return max(sizes) if sizes else 0
