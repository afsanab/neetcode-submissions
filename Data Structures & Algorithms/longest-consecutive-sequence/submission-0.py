class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        mx_len = 0
        index = 0
        curr_len = 0
        while index < (len(nums)-1):
            #check if next val is nums[i]+1
            if nums[index] + 1 == nums[index+1]:
                index +=2
            else:
                if curr_len > mx_len:
                    mx_len = curr_len
                curr_len = 0
                index +=1
            curr_len +=1
        return mx_len


