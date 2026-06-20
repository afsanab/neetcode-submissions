class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in visited:
                return [visited[diff], i]
            else:
                visited[j] = i
            