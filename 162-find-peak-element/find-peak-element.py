class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        low = 0
        high = len(nums)-1
        while low<high:
            mid = (high+low)//2
            if(nums[mid]>nums[mid+1]):
                high = mid
            else:
                low = mid+1
        return low