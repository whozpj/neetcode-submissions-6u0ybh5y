class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLowerBound = 0
        rowUpperBound = len(matrix)-1

        while (rowLowerBound<=rowUpperBound):
            rowMid = (rowLowerBound + rowUpperBound)//2
            if matrix[rowMid][0] <= target and target <= matrix[rowMid][-1]:

                lowerbound = 0
                upperbound = len(matrix[rowMid])-1

                while lowerbound <= upperbound:
                    mid = (upperbound+lowerbound)//2
                    if matrix[rowMid][mid] == target:
                        return True
                    elif matrix[rowMid][mid] < target:
                        lowerbound = mid + 1
                    elif matrix[rowMid][mid] > target:
                        upperbound = mid - 1
                return False
            elif matrix[rowMid][0] < target:#if target higher, increase lowerbound
                rowLowerBound = rowMid + 1
            elif matrix[rowMid][0] > target:#if target is lower, decrease upperbound
                rowUpperBound = rowMid - 1
        return False


