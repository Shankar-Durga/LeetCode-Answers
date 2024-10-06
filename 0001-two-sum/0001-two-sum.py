class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans = {}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in ans:
                return [ans[temp],i]
            ans[nums[i]]=i
        return []
 
