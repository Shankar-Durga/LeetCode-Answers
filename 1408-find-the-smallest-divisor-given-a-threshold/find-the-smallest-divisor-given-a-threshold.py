from math import ceil
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low = 1
        high = max(nums)
        ans = 0
        while low<=high:
            mid = (low+high)//2
            sample = 0
            for i in nums:
                sample += ceil(i/mid)
            if sample<=threshold:
                high = mid-1
                ans = mid
            else:
                low = mid+1
        return ans 