class Solution:
    def isPalindrome(self, s: str) -> bool:
        checker = []
        for i in s:
            if i.isalnum():
                checker.append(i.lower())
        checker = "".join(checker)
        print(checker)
        return checker == checker[::-1]
