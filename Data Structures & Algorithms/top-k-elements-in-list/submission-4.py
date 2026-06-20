class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #make a dictionary of numbers and their frequency
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        # make a bucket sort styled arr: index as frequency, value as arr of nums 
        # with that frequency
        bucket = [[] for i in range(len(nums)+1)]
        for num, frq in freq.items():
            bucket[frq].append(num)
        res = []
        while len(res) < k:
            #if highest frequency is empty - remove it and continue
            if bucket[-1] == []:
                bucket.pop()
            # is not empty - add these values to res, and remove them from bucket
            # so that we can continue moving through the list in reverse
            else:
                for i in bucket[-1]:
                    res.append(i)
                    bucket[-1].remove(i)
        return res
        
