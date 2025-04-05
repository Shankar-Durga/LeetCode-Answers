from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for i in strs:
            checker = [0]*26
            for j in i:
                checker[ord(j) - ord('a')] += 1
            key = tuple(checker)
            ans[key].append(i)
        return list(ans.values())