class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        #find max k
        # keys = list(freq.keys())
        # vals = list(freq.values())
        # an array for each possible frequency
        bucket = [[] for i in range(len(nums)+1)]
        for num, frq in freq.items():
            bucket[frq].append(num)
        res = []
        while len(res) < k:
            if bucket[-1] == []:
                bucket.pop()
            else:
                for i in bucket[-1]:
                    res.append(i)
                    bucket[-1].remove(i)
            # top = max(vals)
            # print(vals, top)
            # index = vals.index(top)
            # vals.remove(top)
            # res.append(keys[index])
            # keys.pop(index)
            # k -=1
        return res
        
