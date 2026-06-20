class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited = set()
        def dfs(r, c):
            area = 0
            #base case - out of bound/"0"/alr visited
            if (r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or
                grid[r][c] == 0 or (r,c) in visited):
                return area
            #recurse to find all other neighbors in this island
            visited.add((r,c))
            area +=1
            area += dfs(r + 1, c)
            area += dfs(r - 1, c)
            area += dfs(r, c + 1)
            area += dfs(r, c - 1)
            return area

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #when we are at an unvisited "1" - this is a new island
                if grid[row][col] == 1 and (row,col) not in visited:
                    curr_area = dfs(row, col)
                    if curr_area > max_area:
                        max_area = curr_area
        return max_area
