class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            #base case
            if i >= len(nums):
                if sorted(subset.copy()) not in res:
                    res.append(sorted(subset.copy()))
                return 
            #add
            subset.append(nums[i])
            dfs(i + 1)
            #not add
            subset.pop()
            dfs(i + 1)
        dfs(0)
        return res
