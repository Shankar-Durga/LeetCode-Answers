class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        data = {}
        i = 0
        result = 0
        for j in range(len(s)):
            if s[j] in data:
                data[s[j]] += 1
            else:
                data[s[j]] = 1
            current_length = (j - i)+1
            max_value = max(data.values())
            if current_length - max_value > k:
                data[s[i]] -= 1
                i += 1 
               
            result = max(result,(j - i)+1)
        return result