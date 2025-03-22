class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        left = 0 
        right = 0
        length = len(s)
        while left < length:
            sample = s[left:right+1]
            if sample == sample[::-1]:
                count += 1
            if right == length - 1:
                left += 1
                right = left
            else:
                right += 1

        return count 