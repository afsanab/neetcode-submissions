class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Plan:
        #find every combination of numbers in the list since there is only 
        #one pair of indices in each set of parameters that would satisfy the condition
        # ex: 0,1 0,2 0,3 1,2 1,3 2,3
        
        #solution attempt
        for index_i, i in enumerate(nums):
            for index_j, j in enumerate(nums):
                if index_i == index_j:
                    continue
                if i+j==target:
                    return sorted([index_i,index_j])
        #this doesnt work beacuse when you search the index it will give you 
        #the first occurance so if index 0 and 1 are the same number you will always get 0
        #so 5 will always get you index 0 for the list [5,5], then this output doesnt come 
        #since your first if statement removes these cases


        #solution from looking at answer:
