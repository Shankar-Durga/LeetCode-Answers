class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==1:
            return 1
        ans = ""
        
        for i in range(len(s)-1): 
            sample = ""
            for j in range(i,len(s)):
                if s[j] not in sample: 
                    sample =sample+s[j] 
                else:
                    break
            if len(sample)>len(ans):
                ans = sample
        return len(ans)            