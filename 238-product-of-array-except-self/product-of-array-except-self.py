class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]*len(nums)
        val = 1
        for i in range(len(nums)):
            ans[i] *= val
            val *= nums[i]
        val = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] *= val
            val *= nums[i]

        return ans
