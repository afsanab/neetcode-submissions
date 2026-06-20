class Graph:
    
    def __init__(self):
        self.adjList = {} # from:to

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adjList:
            self.adjList[src] = set()
        if dst not in self.adjList:
            self.adjList[dst] = set()
        self.adjList[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src in self.adjList:
            if dst in self.adjList[src]:
                self.adjList[src].remove(dst)
                return True
        return False

    def hasPath(self, src: int, dst: int) -> bool:
        #incorrect solution
        # if dst in self.adjList[src]:
        #     return True
        # return False
        #BFS Solution
        queue = deque()
        visited = set()
        queue.append(src)
        while queue:
            curr = queue.popleft()
            
            for neighbor in self.adjList[curr]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(curr)
            if curr == dst:
                return True
        return False
        #DFS Solution

        

