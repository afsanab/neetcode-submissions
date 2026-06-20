class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            # out of bounds
            if i >= len(nums):
                #why the .copy?
                res.append(subset.copy())
                return
            #decision to include nums[i]
            print(subset.append(nums[i]))
            dfs(i + 1)
            #decision not to include nums[i]
            print(subset.pop())
            dfs(i+1)
        dfs(0)
        return res

        