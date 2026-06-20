class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        visited.add((0,0))
        queue.append((0,0))

        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                if r == len(grid) -1 and c == len(grid[0]) -1:
                    return length

                neighbors = [[0,-1], [0,1], [-1,0], [1,0]]
                for dr, dc in neighbors:
                    if (r+dr == len(grid) or c+dc == len(grid[0]) or r + dr < 0 or c + dc < 0 or grid[r + dr][c+dc] == 1 or (r+dr, c + dc) in visited):
                        continue
                    visited.add((r+dr,c+dc))
                    queue.append((r+dr,c+dc))
            length+=1
        #if we havent returned length and we have exited the loop - we never found the path
        return -1