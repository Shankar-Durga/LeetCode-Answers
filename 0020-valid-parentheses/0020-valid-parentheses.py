class Solution:
    def isValid(self, s: str) -> bool:
        data = []
        for i in s:
            if i in "([{":
                data.append(i)
            else:
                if not data or \
                (i == ")" and data[-1]!="(") or \
                (i == "}" and data[-1]!="{") or \
                (i == "]" and data[-1]!="[") :
                    return False
                else:
                    data.pop()
        if(len(data)==0):
            return True
        else:
            return False
