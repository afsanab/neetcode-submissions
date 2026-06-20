"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone = {}
        def dfs(inputNode):
            #base case
            if inputNode in clone:
                return clone[inputNode]
            copy = Node(inputNode.val)
            clone[inputNode] = copy
            for neighbors in inputNode.neighbors:
                copy.neighbors.append(dfs(neighbors))
            return copy
        return dfs(node) if node else None
            