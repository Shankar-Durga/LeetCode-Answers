class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        ans = ""
        c=0
        for i in s:
            if(i=="(" and c>0):
                ans+=i
            elif(i==")" and c>1):
                ans+=i
            c+=1 if i=="(" else -1
        return ans
