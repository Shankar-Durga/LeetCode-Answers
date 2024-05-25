class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            a=x
        else:
             a = -(x)
        b=0
        while a:
            b = b*10+a%10
            a = a//10
        if b>pow(2,31):
             return 0
        
        return(b) if x>=0 else -b
           