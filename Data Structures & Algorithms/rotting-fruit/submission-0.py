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
        while queue:
            #if fruit is alr rotten - rot its neighbors
            row, col = queue.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]
            if grid[row][col] == 1:
                #if fresh - make it rotten - set grid[r][c]=2
                grid[row][col] = 2
                fresh -= 1
            if fresh == 0: 
                return minutes
            for x,y in directions:
                #add its fresh fruit neighbors to queue if not in queue
                if ( row + x >= 0 and col + y >= 0 and row + x < len(grid) and 
                    col + y < len(grid[0]) and (row + x, col + y) not in queue and 
                    grid[row + x][ col + y] == 1):
                    queue.append((row + x, col + y))
            # minutes +=1 each time i add a set of neighbors to the queue
            minutes += 1
        return -1