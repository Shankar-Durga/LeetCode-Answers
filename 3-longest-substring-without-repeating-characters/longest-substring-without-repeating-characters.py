class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = set()
        left = 0
        right = 0
        count = 0
        while right<len(s):

            while s[right] in ans:
                    ans.remove(s[left])
                    left += 1
                    # if temp > count:
                    #     count = temp
                    # temp = right-left

            ans.add(s[right])
            if len(ans)>count:
                count = len(ans)
            right += 1
        if len(ans) > count:
            count = len(ans)
        return count