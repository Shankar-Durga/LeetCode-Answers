class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        while low<=high:
            mid = (high+low)//2
            print(low,mid,high)
            if( low == high ):
                return nums[low]
            if(nums[mid]>=nums[high]):
                low = mid+1
            else:
                high = mid
            