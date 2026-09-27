class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = dict()
        for i in nums:
            prod = 1
            for n in nums:
                if i == n:
                    continue
                else:
                    prod = prod * n
            output[i]= prod
        
        return list(output.values())