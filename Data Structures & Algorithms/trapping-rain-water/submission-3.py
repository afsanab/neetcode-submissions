class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        n = len(height)
        res = 0
        maxleft = [0]*len(height)
        maxright = [0]*len(height)
        for i in range(1, n):
            #store max left
            maxleft[i] = max(height[i-1], maxleft[i-1])
        for i in range(n-2, -1, -1):
            #store max right
            maxright[i] = max(height[i+1], maxright[i+1])
        #find min and - height
        for i in range(n):
            curr_height = min(maxleft[i], maxright[i]) - height[i]
            if curr_height > 0:
                res += curr_height
        return res
                 