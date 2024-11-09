class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        sample = True
        if x<0:
            sample = False
            x =-x
        while True:
            a += x%10
            x = x//10
            if x==0:
                break
            a*=10
        if a > 2**31 - 1 or a < -2**31:
            return 0
        return a if sample else -a  
