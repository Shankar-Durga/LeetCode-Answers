class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i,j in enumerate(nums):
            check = target - j
            
            if check in data:
                return[data[check], i]
            else:
                data[j] = i
