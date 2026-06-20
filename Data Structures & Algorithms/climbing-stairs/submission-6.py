class Solution:
    def climbStairs(self, n: int) -> int:
        #base cases
        if n <= 3:
            return n
        n1 = 2
        n2 = 3
        #make sure to skip base cases her
        for i in range(4, n+1):
            temp = n2
            n2 = n1 + n2
            n1 = temp
        return n2
