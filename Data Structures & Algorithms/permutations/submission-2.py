class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        #base case
        if len(nums) == 0:
            return [[]]
        #create an array without the first element
        # basically - strips down arr to last element (recursively)
        # then builds back up by inserting nums[0] - which is always the "previous"
        # element in the array - into every possible position 
        # until there is not more previous elem
        # then you have all of the permutatons
        subproblems = self.permute(nums[1:])
        res = []

        for i in subproblems:
        #loops every possible position - adds first element in to those positions
            for j in range(len(i) + 1):
                temp = i.copy()
                temp.insert(j, nums[0])
                res.append(temp)
        return res