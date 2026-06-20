import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        for x,y in points: 
            dist = (x**2) + (y**2)
            distances.append([dist, x, y])
        heapq.heapify(distances)
        res = []
        #pop k times from distances, and store x,y in new list to return
        while k>0:
            d,x,y = heapq.heappop(distances)
            res.append([x, y])
            k-=1
        return res

        