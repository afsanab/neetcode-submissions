# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


#attempted but could not solve by myself - followed vid
class Solution:
     def diameterOfBinaryTree(self, root: TreeNode) -> int:
        #global var
        self.mxdiameter = 0
        def dfs(root):
            #base case
            if not root:
                return 0
            #calculate height of left and right
            left = dfs(root.left)
            right = dfs(root.right)
            #sum of left height + right height = curr diameter
            #check if curr diamter is > max diameter
            self.mxdiameter = max(self.mxdiameter, left + right)
            #return curr max height, max of r/l + 1 for curr node
            return 1 + max(left, right)
        #run the func with root to traverse tree dfs
        dfs(root)
        return self.mxdiameter