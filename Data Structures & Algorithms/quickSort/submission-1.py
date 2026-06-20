# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        return self.quicksortHelper(pairs, 0, len(pairs)-1)
    
    def quicksortHelper(self, pairs, s, e) -> List[Pair]:
        #base case
        if e-s <= 0:
            return pairs
        pivot = pairs[e]
        left = s
        for i in range(s,e):
            if pairs[i].key < pivot.key:
                temp = pairs[left]
                pairs[left] = pairs[i]
                pairs[i] = temp
                left +=1
        pairs[e] = pairs[left]
        pairs[left] = pivot

        self.quicksortHelper(pairs, s, left - 1) 
        self.quicksortHelper(pairs, left + 1, e)   

        return pairs            