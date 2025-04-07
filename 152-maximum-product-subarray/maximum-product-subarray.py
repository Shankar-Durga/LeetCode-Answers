class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre = 1
        suf = 1
        length = len(nums)
        ans = nums[0]
        for i in range(length ):
            if pre == 0: pre = 1
            if suf == 0: suf = 1
            pre *= nums[i]
            suf *= nums[(length)-i-1]
            ans = max(ans, max(pre,suf))
        return ans