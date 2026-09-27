class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        # loop the arr height
        for i in range(len(height)-1):
            # water can never be stored in i==0
            if i == 0:
                continue
            # if no left wall exists - continue
            elif height[i-1] < height[i]:
                continue
            elif height[i-1] > height[i]:
                # if left and right are taller than curr - width of 1
                if i+1 < len(height) and height[i-1] < height[i+1]:
                    water += min(height[i-1], height[i+1]) - height[i]
                # no direct right wall - continue
                # add volume of lower x width/dist
                j = i
                while j<(len(height)-1):
                    if height[j] > height[i]:
                        water += min(height[i], height[j])*(j-i)
                    j+=1                
            i+=1
        return water

