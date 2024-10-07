class Solution:
    def climbStairs(self, n: int) -> int:
        prev,cur = 0,1
        for i in range(n):
            temp = cur
            cur = prev+cur
            prev = temp
        return cur
        