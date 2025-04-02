class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = 0
            value = i
            while value:
                if value&1:
                    count += 1
                value>>=1
            ans.append(count)
        return ans