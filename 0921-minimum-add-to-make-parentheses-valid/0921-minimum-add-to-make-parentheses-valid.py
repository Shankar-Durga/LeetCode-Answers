class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opener = 0
        closer = 0
        for i in s:
            if(i == "("):
                opener+=1
            elif(i == ")" and opener>0):
                opener-=1
            else:
                closer+=1
        return opener+closer
        