class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1
        ans = 0
        for i in range(n):
            ans = prev + cur
            prev = cur
            cur = ans 
        return ans
            