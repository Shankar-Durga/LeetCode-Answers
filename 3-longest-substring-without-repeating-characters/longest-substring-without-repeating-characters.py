class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        data_set = set()
        left = 0
        result = 0
        for right in range(len(s)):
            while s[right] in data_set:
                data_set.remove(s[left])
                left+=1
            data_set.add(s[right])
            result = max(result, (right-left)+1)
        return result 
            