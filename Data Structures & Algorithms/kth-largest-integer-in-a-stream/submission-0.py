class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        nums_2 = sorted(self.nums)
        for i in range(self.k - 1):
            nums_2.pop()
        return max(nums_2)

