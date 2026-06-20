class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        r = 0
        c = 0
        visited = set()
        def dfs(grid, r, c, visited):
            # out of bounds/reached a 1/
            # reached a visited is a base case
            if r >= len(grid) or c >= len(grid[0]) or r < 0 or c < 0 or grid[r][c] == 1 or (r,c) in visited:
                return 0
            # reached bottom right is a base case
            #why return 0 at a base case? no valid paths from here
            elif r == len(grid)-1 and c == len(grid[0])-1:
                return 1
            #keep record of curr visited node to not repeat it bc if we
            #are at this line we havent returned and need
            #TO Keep looking for next coord
            visited.add((r,c))
            #recurse in all 4 directionsto check for all 
            #possible paths, and it will return num possible paths 
            count = 0
            count += dfs(grid, r + 1, c, visited)
            count += dfs(grid, r - 1, c, visited)
            count += dfs(grid, r, c + 1, visited)
            count += dfs(grid, r, c - 1, visited)
            #remove this coord from visit (backtracking)
            visited.remove((r,c))
            #return num paths
            return count
        return dfs(grid, r,c, visited)

