class Solution:
    def longestPalindrome(self, s: str) -> int:
        sample = []
        length = 0
        for i in s:
            if i in sample:
                length+=2
                sample.remove(i)

            else:
                sample.append(i)
        if sample:
            length+=1
        return length