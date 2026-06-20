class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        #find max k
        keys = list(freq.keys())
        vals = list(freq.values())
        res = []
        while k > 0:
            top = max(vals)
            print(vals, top)
            index = vals.index(top)
            vals.remove(top)
            res.append(keys[index])
            keys.pop(index)
            k -=1
        return res
        
