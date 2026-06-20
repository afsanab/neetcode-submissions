class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_2 = set(nums)
        if len(nums_2) !=  len(nums):
            return True
        else:
            return False
        