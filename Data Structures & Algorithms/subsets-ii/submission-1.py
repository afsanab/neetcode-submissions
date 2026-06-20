class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #my solution - not the best
        # res = []
        # subset = []
        # def dfs(i):
        #     #base case
        #     if i == len(nums):
        #         if sorted(subset.copy()) not in res:
        #             res.append(sorted(subset.copy()))
        #         return 
        #     #add
        #     subset.append(nums[i])
        #     dfs(i + 1)
        #     #not add
        #     subset.pop()
        #     dfs(i + 1)
        # dfs(0)
        # return res

        res = []
        nums.sort()
        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset.copy())
                return
            # to include 
            subset.append(nums[i])
            backtrack(i + 1, subset)
            # to not include
            subset.pop()
            #skipping dupes
            while i + 1 < len(nums) and nums[i] == nums[i+1]:
                i +=1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res