class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,n in enumerate(numbers):
            diff = target-n
            if diff in numbers and numbers.index(diff)!= i:
                return sorted([i+1,numbers.index(diff)+1])
        