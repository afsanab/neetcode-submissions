import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [ -x for x in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = stones[0]
            y = stones[1]
            heapq.heappop(stones)
            heapq.heappop(stones)
            print(x, y)
            if x < y:
                new = (x-y)
                heapq.heappush(stones, new)
        if stones:
            return abs(stones[0])
        else:
            return 0