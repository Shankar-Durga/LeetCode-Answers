class Solution:
    def sorting_value(self,nums, low, mid, high):
        left = low
        right = mid+1
        sample = []
        while left <= mid and right<=high:
            if(nums[left]<nums[right]):
                sample.append(nums[left])
                left+=1
            else:
                sample.append(nums[right])
                right+=1
        while left<=mid:
            sample.append(nums[left])
            left+=1
        while right<=high:
            sample.append(nums[right])
            right+=1
        nums[low:high+1] = sample
        # for i in range(len(sample)):
        #     nums[low+i] = sample[i]


 

    def merge_sort(self,nums, low, high):
        if low==high:
            return
        mid = (low+high)//2
        self.merge_sort(nums, low, mid)
        self.merge_sort(nums, mid+1, high)
        self.sorting_value(nums, low, mid, high)


    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        low = 0
        high = len(nums) - 1
        self.merge_sort(nums, low, high)
        print(nums)
        return nums