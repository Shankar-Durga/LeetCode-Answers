class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        element = 0
        length = len(nums)
        for i in range(length):
            if(element == 0 or count == 0):
                element = nums[i]
                count = 1
            elif(element == nums[i]):
                count+=1
            elif(element != nums[i]):
                count -=1
        return element