class Solution:
    def rob(self, nums: List[int]) -> int:
        evens = 0
        odds = 0
        #evens
        for i in range(0, len(nums),2):
            evens += nums[i]
        for i in range(1, len(nums),2):
            odds += nums[i]

        return max(evens, odds)