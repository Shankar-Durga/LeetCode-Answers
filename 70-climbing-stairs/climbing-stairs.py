class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 0
        cur = 1
        ans = 0
        for i in range(n):
                temp = cur
                cur = prev + cur
                prev = temp
        return cur 