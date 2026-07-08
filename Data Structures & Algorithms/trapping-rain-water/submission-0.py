class Solution:
    def trap(self, height: List[int]) -> int:
        

        #initialize a left pointer, and a right pointer, close to each other

        left = 0
        right = len(height)-1

        maxLeft = height[left]
        maxRight = height[right]

        result = 0


        while left < right:

            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft, height[left])

                result += maxLeft - height[left]

                
            else:
                right -=1
                maxRight = max(maxRight, height[right])

                result += maxRight - height[right]
        

        return result

                

