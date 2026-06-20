class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        visited.add((0,0))
        queue.append((0,0))

        length = 0
        # until queue is empty and all neighbors have been visited
        while queue:
            for i in range(len(queue)):
                #get top neighbor and check if it is the destination
                r,c = queue.popleft()
                if r == len(grid) -1 and c == len(grid[0]) -1:
                    return length
                # then check all of its neighbors
                neighbors = [[0,-1], [0,1], [-1,0], [1,0]]
                # skip(continue) all invalid neighbors
                for dr, dc in neighbors:
                    if (r+dr == len(grid) or c+dc == len(grid[0]) or r + dr < 0 or c + dc < 0 or grid[r + dr][c+dc] == 1 or (r+dr, c + dc) in visited):
                        continue
                    # if it isnt invalid then add it to the queue and we will visit it later
                    # to check if it is destination - if its not it will still add to len until we 
                    # reach the destination along that path - if we get to a point on that path and 
                    # dont have any moves left and not at dest - it will not be valid and wont return len
                    visited.add((r+dr,c+dc))
                    queue.append((r+dr,c+dc))
            length+=1
        #if we havent returned length and we have exited the loop - we never found the path
        return -1