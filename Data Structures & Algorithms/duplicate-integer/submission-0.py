class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        no_dupes = set(nums)
        if len(no_dupes) < len(nums):
            return True
        else:
            return False

        