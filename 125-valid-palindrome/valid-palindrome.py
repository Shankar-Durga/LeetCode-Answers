class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = [char.lower() for char in s if char.isalnum()]
        filtered_s = ''.join(filtered_chars) 

        
        return filtered_s == filtered_s[::-1]
