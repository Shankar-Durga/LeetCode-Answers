# from collections import deafultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = {}
        buckets = [[] for _ in range(len(nums) + 1)]
        ans = []
        count = 0
        left = 0
        right = 0
        
        for i in nums:
            if i in a:
                a[i] += 1
            else:
                a[i] = 1
            
        for key, value in a.items():
            buckets[value].append(key)
         
        for i in range(len(nums),-1,-1):
            if len(ans) == k:
                break
            if buckets[i]:
                ans.extend(buckets[i])
        return ans
        
