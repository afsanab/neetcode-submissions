class Solution:
    def rob(self, nums: List[int]) -> int:
        # evens = 0
        # odds = 0
        # for i in range(0, len(nums),2):
        #     evens += nums[i]
        # for i in range(1, len(nums),2):
        #     odds += nums[i]

        # return max(evens, odds)
        rob1, rob2 = 0, 0 # x1,x2, ...., rob1, rob2, n, n+1, ...
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1=rob2
            rob2=temp #rob2 becomes n! shift over all roles and repeat process
        return rob2