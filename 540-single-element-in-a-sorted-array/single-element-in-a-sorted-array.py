class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        
        low = 0 
        high = len(nums)-1

        while low<=high:
            if(nums[low] == nums[low+1]):
                low+=2
            else:
                return nums[low]
            if(nums[high] == nums[high-1]):
                high -= 2
            else:
                return nums[high]
        