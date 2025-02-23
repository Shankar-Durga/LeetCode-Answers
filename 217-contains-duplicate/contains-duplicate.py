class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        data = {}
        for i in range(len(nums)):
            if nums[i] in data:
                return True
            data[nums[i]] = 1 
        return False