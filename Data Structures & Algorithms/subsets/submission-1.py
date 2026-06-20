class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [] # final set of subsets
        subset = [] # per round, to be added to res
        def dfs(i):
            # out of bounds
            if i >= len(nums):
                #why the .copy? - because subset is out of the function
                res.append(subset.copy())
                return
            #decision to include nums[i] - add it to curr subset, and run dfs again
            # with the subset alr containing nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            #decision not to include nums[i] - getting an empty subset
            #pops added num and moves forward
            subset.pop()
            dfs(i+1)
        dfs(0)#starts at index 0
        return res

        