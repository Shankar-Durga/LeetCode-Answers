class Solution:
    def isValid(self, s: str) -> bool:
        
        validator = "([{"
        stack = []
        for i in s:
            if i =='(' or i=='[' or i== '{':
                stack.append(i)
            elif not stack:
                return False
            elif i == ")":
                if stack[-1]!="(":
                    return False
                else:
                    stack.pop(-1)
            elif i == "]":
                if stack[-1]!="[":
                    return False
                else:
                    stack.pop(-1)
                
            elif i == "}":
                if stack[-1]!="{":
                    return False
                else:
                    stack.pop(-1)
        if stack:
            return False
        return True
                