class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()

        queue.append((0,0))
        visited.add((0,0))
        length = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                #reached bottom right node
                if r == len(grid)-1 and c == len(grid[0])-1:
                    return length
                
                neighbors = [[0,1], [0,-1], [1,0], [-1,0]]
                for x, y in neighbors:
                    neigh_row = r + x
                    neigh_col = c + y
                    #check out of bounds
                    if (neigh_row < 0 or neigh_col < 0 or
                       neigh_row == len(grid) or neigh_col == len(grid[0]) or
                       (neigh_row, neigh_col) in visited or grid[neigh_row][neigh_col] == 1):
                       continue
                    queue.append((neigh_row, neigh_col))
                    visited.add((neigh_row, neigh_col))
            length +=1
        return -1
            