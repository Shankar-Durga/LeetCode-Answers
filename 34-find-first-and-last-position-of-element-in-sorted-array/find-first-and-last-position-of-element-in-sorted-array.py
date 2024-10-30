class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(x):
            length = len(nums)
            low = 0
            high = length
            while low < high:
                mid = (high+low)//2
                if nums[mid]<x:
                    low = mid+1
                else:
                    high = mid
            return low
        
        low = search(target)
        high = search(target+1)-1
        if low<=high:
            return [low,high]
        return [-1,-1]
        

        
                