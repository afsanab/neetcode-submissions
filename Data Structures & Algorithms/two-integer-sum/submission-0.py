class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #find every combination of numbers in the list since there is only 
        #one pair of indices in each set of parameters that would satisfy the condition
        # ex: 0,1 0,2 0,3 1,2 1,3 2,3
        for i in nums:
            for j in nums:
                if i == j:
                    continue
                if i+j==target:
                    return sorted([nums.index(i),nums.index(j)])
