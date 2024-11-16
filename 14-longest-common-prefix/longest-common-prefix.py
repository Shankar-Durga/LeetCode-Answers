class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = len(strs[0])
        for i in strs:
            if min_length>len(i):
                min_length = len(i)
        ans = ""
        for i in range(min_length):
            checker = True
            for j in range(1,len(strs)):
                if(strs[0][i] != strs[j][i] ):
                    checker = False
                    break
            if checker == False:
                break
            else:
                ans+=strs[0][i]
        return ans
        