class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []
        candidates.sort()  # Sort the candidates to handle duplicates more easily

        def dfs(i, total):
            # If we've hit the target, append a copy of the subset to the result
            if total == target:
                res.append(subset[:])  # Add a copy of subset
                return

            # If we've exceeded the target or run out of elements, stop the recursion
            if i >= len(candidates) or total > target:
                return

            # Include the current candidate
            subset.append(candidates[i])
            dfs(i + 1, total + candidates[i])

            # Exclude the current candidate and skip duplicates
            subset.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, total)

        dfs(0, 0)
        return res
