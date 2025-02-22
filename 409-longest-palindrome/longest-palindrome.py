class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = []
        count=0
        for i in s:
            if i in a:
                a.remove(i)
                count+=2
            else:
                a.append(i)
        if a:
            return count+1
        else:
            return count