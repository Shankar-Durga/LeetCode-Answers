class Solution:
    def scoreOfString(self, s: str) -> int:
        data = []
        count = 0
        for i in s:
            data.append(ord(i))
        for i in range(len(data)-1):
            count += abs(data[i]-data[i+1])
        return count