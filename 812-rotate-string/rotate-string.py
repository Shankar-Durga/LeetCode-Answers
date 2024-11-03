class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if (len(s)!=len(goal)):
            return False
        data = s+s
        if (goal in data):
            return True
        else:
            return False 
        #s+s adding string twice will make all possible rotational output in code