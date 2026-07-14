class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        if obstacleGrid[m-1][n-1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]

        dp[m-1][n-1] = 1



        for row in range(m-1, -1, -1):
            for col in range(n-1,-1,-1):

                if obstacleGrid[row][col] == 1:
                    continue
                
                if row + 1 < m and col + 1 < n:
                    dp[row][col] = dp[row+1][col] + dp[row][col+1]
                elif row + 1 < m:
                    dp[row][col] = dp[row+1][col]
                elif col + 1 < n:
                    dp[row][col] = dp[row][col+1]
        return dp[0][0]