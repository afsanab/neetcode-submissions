class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:

        def dfs(grid, row, col, visited):
            #base case 1: no where left to go - out of bounds
            if (min(row,col) < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] == 1 or (row,col) in visited):
                return 0
            #base case 2: reached end
            if row == len(grid) - 1 and col == len(grid[0]) - 1:
                return 1

            #recurse
            visited.add((row, col))

            count = 0
            count += dfs(grid, row - 1, col, visited)
            count += dfs(grid, row + 1, col, visited)
            count += dfs(grid, row, col - 1, visited)
            count += dfs(grid, row, col + 1, visited)

            visited.remove((row, col))
            return count

        return dfs(grid, 0, 0, set())


        