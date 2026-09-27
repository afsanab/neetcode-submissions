class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #double for loop
        length = 1
        for n in nums:
            curr_len = 1
            prev = n
            for m in nums[n:]:
                if m > prev:
                    curr_len += 1
                    prev = m
            if curr_len > length:
                length = curr_len
        return length