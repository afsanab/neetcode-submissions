class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #double for loop
        length = 1
        curr = len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            if nums[curr] > nums[i-1]:
                length +=1
                curr = i-1
            else:
                i -=1
        return length
        
            