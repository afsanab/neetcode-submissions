class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #attempt 1
        # output = []
        # for i in nums:
        #     prod = 1
        #     for n in nums:
        #         if i == n:
        #             continue
        #         else:
        #             prod = prod * n
        #     output.append(prod)
        # return output
        
        
        #attempt 2
        # product = 1
        # for i in nums:
        #     product = product*i
        # output = [product] * len(nums)
        # for index,out in enumerate(output):
        #     print(out)
        #     print(nums[index])
        #     output[index] = int(out/nums[index])
        # return output

        res = [1] * (len(nums))
        
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
