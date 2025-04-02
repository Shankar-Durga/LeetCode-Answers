class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0]*(n+1)
        ans[0] = 0
        for i in range(1,n+1):
            count = 0
            ans[i] = ans[i>>1]+(i&1)
        return ans
        # my approach
        # count = 0
        #     value = i
        #     while value:
        #         if ans[value]!=0:
        #             count += ans[value]
        #             break
        #         elif value&1:
        #             count+=1
        #         value>>=1
        #     ans[i]=count
        # return ans