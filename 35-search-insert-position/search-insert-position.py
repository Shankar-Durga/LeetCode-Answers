class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        output = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return i
            if nums[i]<target:
                output = i+1
        return output
            