class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output=[]
        diffs = {} # 0-sum | (i1,i2)
        #get every combo, and search 3rd val
        for i, n1 in enumerate(nums):
            for j, n2 in enumerate(nums):
                if i==j:
                    continue
                s = i+j
                diffs[-s] = [i,j]
        for i in nums:
            if i in nums:
                triplet = diffs[i]
                sorted(triplet.append(i))
                if triplet not in output:
                    output.append(triplet)
        return output
