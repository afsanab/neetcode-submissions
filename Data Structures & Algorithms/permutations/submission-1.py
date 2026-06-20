class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case
        if len(nums) == 0:
            return [[]]
        #create an array without the first element
        subproblems = self.permute(nums[1:])
        #add the curr elem to every position
        res = []
        #dont fully understand this part :/
        for i in subproblems:
            for j in range(len(i) + 1):
                temp = i.copy()
                temp.insert(j, nums[0])
                res.append(temp)
        return res