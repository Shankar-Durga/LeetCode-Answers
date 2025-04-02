class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            count = 0
            value = i
            while value:
                if len(ans)<value:
                    count += ans[value+1]
                    break
                elif value&1:
                    count += 1
                value>>=1
            ans.append(count)
        return ans