class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh = 0
        #add all rotten fruit to a queue
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    fresh +=1
                if grid[r][c] == 2:
                    queue.append((r,c))
        minutes = 0
        directions = [[1,0], [-1,0], [0,1], [0,-1]]
        while queue and fresh > 0:
            #if fruit is alr rotten - rot its neighbors
            for i in range(len(queue)):
                row, col = queue.popleft()
                for x,y in directions:
                    #add its fresh fruit neighbors to queue if not in queue
                    if (row + x >= 0 and col + y >= 0 and row + x < len(grid) and 
                        col + y < len(grid[0]) and (row + x, col + y) not in queue and 
                        grid[row + x][ col + y] == 1):
                        queue.append((row + x, col + y))
                        grid[row + x][col + y] = 2
                        fresh -=1
            # minutes +=1 each time i add a set of neighbors to the queue
            minutes += 1
        return minutes if fresh == 0 else -1
