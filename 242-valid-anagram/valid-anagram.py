class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        data1 = {}
        data2 = {}
        for i in range(len(s)):
            if s[i] not in t:
                return False
            if s[i] in data1:
                data1[s[i]] += 1
            else:
                data1[s[i]] = 1
            if t[i] in data2:
                data2[t[i]] += 1
            else:
                data2[t[i]] = 1
        for i in s:
            if data1[i] != data2[i]:
                return False
        return True