class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        def getSum(li):
            s = 0
            for i in li:
                s += i
            return s
        def dfs(i):
            #base case/out of bounds
            if i >= len(nums):
                return
            #less than 9 so keep adding
            if getSum(subset) < target:
                #add the same number
                subset.append(nums[i])
                dfs(i)
                #move on to the next number
                subset.pop()
                dfs(i+1)
            # == 9 means its a subset to add to res
            elif getSum(subset) == target:
                if subset not in res:
                    res.append(subset.copy())
                dfs(i+1)
            #>9
            elif getSum(subset) > target:
                dfs(i+1)
        dfs(0)
        return res
                