from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = defaultdict(int)
        buckets = [[] for _ in range(len(nums)+1)]
        ans = []
        
        for i in nums:
            a[i] += 1
            
        for key, value in a.items():
            buckets[value].append(key)

        for i in range(len(nums),-1,-1):
            if len(ans) == k:
                break
            if buckets[i]:
                ans.extend(buckets[i])
        return ans
        
