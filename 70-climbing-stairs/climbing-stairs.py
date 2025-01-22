class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1
        for i in range(n):
            sample = cur
            cur = prev + cur 
            prev = sample
        return cur