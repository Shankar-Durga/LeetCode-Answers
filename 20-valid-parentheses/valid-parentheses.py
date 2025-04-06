class Solution:
    def isValid(self, s: str) -> bool:
        validator = {'(':')', '{':'}', '[':']'}
        stack = []
        for i in s:
            if i in "{([":
                stack.append(i)
            elif not stack or validator[stack.pop()] != i:
                return False
        if stack:
            return False
        return True