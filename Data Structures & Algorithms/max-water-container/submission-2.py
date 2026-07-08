class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights)-1
        maxWater = 0

        while start<end:
            water = (end-start) * min(heights[start],heights[end])
            maxWater = max(water,maxWater)

            if heights[start]<=heights[end]:
                start+=1
            else:
                end -=1
        return maxWater
