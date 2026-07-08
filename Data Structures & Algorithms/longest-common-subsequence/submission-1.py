class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        grid = [[0] * (len(text2) + 1) for _ in range(len(text1)+1)]

        #text1 = row
        #text2 = col


        for row in range(len(text1)-1,-1,-1):
            for col in range(len(text2)-1,-1,-1):
                if text1[row] == text2[col]:
                    grid[row][col] = grid[row+1][col+1] + 1
                else:
                    grid[row][col] = max(grid[row][col+1], grid[row+1][col])
        return grid[0][0]