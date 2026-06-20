class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        res = []
        subset = []
        def dfs(i):
            #reached sum
            if sum(subset) == target and subset not in res:
                res.append(subset.copy())
                return
            #out of bound/base case
            if i >= len(candidates):
                return
            #passed sum
            if sum(subset) > target:
                return
            #less than sub - keep adding
            subset.append(candidates[i])
            dfs(i+1)
            subset.pop()
            #skip duplicates
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i+1)
        dfs(0)
        return res