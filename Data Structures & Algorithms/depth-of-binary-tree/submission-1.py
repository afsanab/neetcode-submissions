# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root:TreeNode) -> int:
        #my initial solution - DFS recursive 
        # if not root:
        #     return 0
        # depth = 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # return depth

        #BFS solution - followed vid
        # if not root:
        #     return 0
        # level = 0
        # q = deque([root])
        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left:
        #             q.append(node.left)
        #         if node.right:
        #             q.append(node.right)
        #     level +=1
        # return level

        #DFS iterative - followed vid
        stack = [[root,1]]
        mxDepth = 0
        while stack: #not empty
            node, depth = stack.pop()
            if node:
                mxDepth = max(mxDepth, depth)
                stack.append([node.left, depth +1])
                stack.append([node.right, depth +1])
        return mxDepth