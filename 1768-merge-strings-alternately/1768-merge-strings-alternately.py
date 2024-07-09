class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = len(word1)
        b = len(word2)
        sample = ""
        for i in range(a if a>=b else b):
            if(i<a):
                sample += word1[i]
            if(i<b):
                sample += word2[i]
        return sample 
        