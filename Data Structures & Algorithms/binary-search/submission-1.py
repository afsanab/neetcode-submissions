class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while l<=r:
            m = (l + r) // 2 # dont fully get this yet
            if nums[m] > target:
                r = m -1 
            elif nums[m] < target:
                l = m + 1
            else:
                return m # m = target
        return -1 # if r is greater than l, we have searched the arr and target
                    # was not found