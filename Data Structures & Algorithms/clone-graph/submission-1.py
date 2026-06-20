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
            #if clone exists - return clone
            if inputNode in clone:
                return clone[inputNode]
            # else create a clone of te node
            copy = Node(inputNode.val)
            # log the old node and map it to the new node
            clone[inputNode] = copy
            #then recurse to make a copy of each neighbor, and log it, 
            # and then appen the return val(the copied node) to the curr node's neighbors
            for neighbors in inputNode.neighbors:
                copy.neighbors.append(dfs(neighbors))
            return copy
        return dfs(node) if node else None
            