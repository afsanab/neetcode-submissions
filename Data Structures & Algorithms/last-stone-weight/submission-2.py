import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -x for x in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            x = stones[0]*(-1)
            y = stones[1]*(-1)
            if x == y:
                heapq.heappop(stones)
                heapq.heappop(stones)
            elif x < y:
                new = (y-x)*(-1)
                heapq.heappop(stones)
                heapq.heappop(stones)
                heapq.heappush(stones, new)
            else:
                new = (x-y)*(-1)
                heapq.heappop(stones)
                heapq.heappop(stones)
                heapq.heappush(stones, new)
        if stones:
            return abs(stones[0])
        else:
            return 0