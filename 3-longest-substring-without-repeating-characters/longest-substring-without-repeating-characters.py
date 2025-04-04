class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        length = 0
        left = 0
        right = 0
        for i in s:
            if i not in substring:
                substring.add(i)
                right += 1
                length = max(length, len(substring))
            else:
                while i in substring:
                    substring.remove(s[left])
                    left += 1 
                substring.add(i)
        return length
