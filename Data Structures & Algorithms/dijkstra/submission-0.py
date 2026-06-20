class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # populate an adjacency list given the edges
        adj = {}
        for i in range(n):
            adj[i] = []
        print(n)
        # u is src, v is dest, w is weight
        for u,v,w in edges:
            adj[u].append([v, w])
        # traverse adj list to get the graph - update the weight as u go to get min on shortest
        # minheap/pqueue instead of a queue bc you want to travel to the closest node each time obv
        shortest = {}
        minheap = [[0, src]]
        while minheap:
            w1, n1 = heapq.heappop(minheap)
            if n1 in shortest:
                continue
                # we know this is the shortest bc minheap will sort it by shortest weight
            shortest[n1] = w1
        # for the adjacency list for n1(curr node) we have a list of tuples[node, weight]
        # if this next node is not yet in shortest - add it to heap with the curr n1 weight + new node weight to n1
        # bc even if its not the shortest we know its a valid path
        # we can update if a shorter path is found
            for n2, w2 in adj[n1]:
                if n2 not in shortest:
                    heapq.heappush(minheap, [w1 + w2, n2])
        
        # empty values
        for i in range(n):
            if i not in shortest:
                shortest[i] = -1

        return shortest