class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 0
        temp = 0
        nums.sort()
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i]-1 == nums[i-1]:
                temp += 1
            else:
                temp = 0
            count = max(temp, count)
        
        return count+1