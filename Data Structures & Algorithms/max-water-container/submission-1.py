class Solution:
    def maxArea(self, heights: List[int]) -> int:
        len1 = len(heights)
        left = 0
        right = len1-1
        area =0
        while(left < right):
            width = right - left
            heights1 = min(heights[left],heights[right])
            area = max (area,width * heights1)

            if (heights[left]<heights[right]):
                left += 1
            else:
                right -= 1
            
        return area
            
        