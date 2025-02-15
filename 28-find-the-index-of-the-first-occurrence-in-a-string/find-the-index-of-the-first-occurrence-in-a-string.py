class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        check = len(needle)
        for i in range(len(haystack)):
            sample = i+check
            if haystack[i:sample] == needle:
                return i
        return -1