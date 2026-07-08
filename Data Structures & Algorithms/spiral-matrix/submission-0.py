class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        result = []


        right = len(matrix[0])-1
        left = 0
        
        top = 0
        bottom = len(matrix) - 1


        while left <= right and top <= bottom:

            #print top row
            for i in range(left, right+1):
                result.append(matrix[top][i])
            top += 1

            #print rightSide
            for i in range(top, bottom+1):
                result.append(matrix[i][right])
            right -= 1
            #print bottom reversed
            if top <= bottom:
                for i in range(right, left -1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            #print left side reversd
            if left <= right:
                for i in range(bottom, top-1, -1):
                    result.append(matrix[i][left])
                left += 1
        return result

            