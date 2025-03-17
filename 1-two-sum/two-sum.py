class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val = {}
        for index, value in enumerate(nums):
            sample = target - value
            if sample in val:
                return (val[sample], index)
            val[value] = index 
