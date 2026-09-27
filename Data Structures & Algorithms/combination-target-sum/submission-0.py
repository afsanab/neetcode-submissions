class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def getSum(nums):
            s = 0
            for i in nums:
                s += i
            return s
        def dfs(i):
            #base case/out of bounds
            if i >= len(nums):
                return
            #less than 9 so keep adding
            if getSum(subset) < 9:
                #add the same number
                subset.append(nums[i])
                dfs(i)
                #move on to the next number
                subset.pop()
                dfs(i+1)
            # == 9 means its a subset to add to res
            elif getSum(nums) == 9:
                res.append(subset.copy())
                subset.pop()
                dfs(i+1)
            #>9
            else:
                subset.pop()
                dfs(i+1)
        return res
                