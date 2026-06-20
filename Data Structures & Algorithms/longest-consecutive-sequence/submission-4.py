class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_len = 0
        index = 0

        while index < len(nums):
            #if num is not beginning of sequence
            if (nums[index] -1) in nums_set:
                index +=1
                continue
            curr_len = 1
            #if next elem == i +1
            curr_num =  nums[index]+1
            while curr_num in nums_set:
                curr_len +=1
                curr_num +=1
            #if next elem not found
            if curr_len > max_len:
                max_len = curr_len
            curr_len = 1
            index +=1
        return max_len

