class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data ={}
        for index, value in enumerate(nums):
            checker = target - value
            if checker in data:
                return([data[checker], index])
            data[value] = index
        