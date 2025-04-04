class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = []
        length = 0
        for i in s:
            if i not in substring:
                substring.append(i)
                length = max(length, len(substring))
            else:
                while i in substring:
                    substring.pop(0)
                substring.append(i)
        return length
