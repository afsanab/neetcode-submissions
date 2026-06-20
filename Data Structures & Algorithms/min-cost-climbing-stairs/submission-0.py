class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #goes backwards from the 2nd to last to the first
        #then checks how much it costs to go to the next 2 and adds the min cost
        #this continues backwards so you get the entire path cost
        #then you just pick if its cheaper to start at 0 or 1
        cost.append(0)
        for i in range(len(cost) - 3, -1, -1):
            cost[i] += min(cost[i + 1], cost[i + 2])
        return min(cost[0], cost[1])

        #backwards tree, fill in the lowest cost from that index to the end point, 
        #then since we can only start at 1 or 2 the minimum or 1 or 2 is the answer 
        #of lowest tot cost