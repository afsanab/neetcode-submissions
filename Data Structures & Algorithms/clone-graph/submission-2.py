"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        # keep track of what u have already copied with res
        res = {}
        # add all neighbors that havent been copied to queue
        q = deque()
        root = Node(node.val)
        res[node] = root
        for neighbor in node.neighbors:
            q.append(neighbor)
        while q:
            curr = q.pop()
            if curr not in res:
                copy = Node(curr.val)
                res[curr] = copy
                for neighbor in curr.neighbors:
                    if neighbor not in res:
                        q.append(neighbor)
        # go back and connect all neighbors using res map
        for og in res:
            temp = []
            for n in og.neighbors:
                temp.append(res[n])
            res[og].neighbors = temp
        return root