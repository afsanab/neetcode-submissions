class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lengths = [1] * len(nums)
        for i in range(len(nums) -1, -1, -1):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    lengths[i] = max(lengths[i], 1+lengths[j])
        return max(lengths)
        
            