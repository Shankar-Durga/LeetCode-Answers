class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j,k = i+1,len(nums)-1
            sample = nums[i]
            while j<k:
                checker = sample + nums[j] + nums[k]
                if  checker == 0:
                    ans.append([sample, nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k-=1
                elif checker > 0:
                    k -= 1
                else:
                    j +=1 
        return ans
                