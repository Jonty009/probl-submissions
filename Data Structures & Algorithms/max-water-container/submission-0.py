class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area, l, r = 0, 0, len(heights)-1
        while l<r:
            min_height = min(heights[l], heights[r])
            current_area = (r-l) * min_height
            if current_area > max_area:
                max_area = current_area
            if heights[l] < heights[r]:
                l += 1
            else: 
                r -= 1
        return max_area
