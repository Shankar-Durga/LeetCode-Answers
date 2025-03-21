class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 1):
            return nums[0]
        sample = [0]*n
        sample[0] = nums[0]
        sample[1] = max(nums[0],nums[1])
        for i in range(2,n):
            sample[i] = max(sample[i-1],abs(sample[i-2]+nums[i]))
        return sample[-1]

           