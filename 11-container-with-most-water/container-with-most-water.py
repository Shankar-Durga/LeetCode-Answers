class Solution:
    def maxArea(self, height: List[int]) -> int:
        most_water = 0
        left = 0
        right = len(height)-1
        while left<right:
            min_value = min(height[left], height[right])
            most_water = max(min_value*(right - left), most_water)
            if height[left]<height[right]:
                left += 1
            else:
                right -=1  
        return most_water