import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -x for x in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            x = heapq.heappop(stones)*(-1)
            y = heapq.heappop(stones)*(-1)
            if x < y:
                new = (y-x)*(-1)
                heapq.heappush(stones, new)
            else:
                new = (x-y)*(-1)
                heapq.heappush(stones, new)
        if stones:
            return abs(stones[0])
        else:
            return 0