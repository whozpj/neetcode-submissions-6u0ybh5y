class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        

        def merge(leftArr, rightArr):
            li = 0
            ri = 0
            final = []
            while li < len(leftArr) or ri < len(rightArr):

                if li < len(leftArr) and ri < len(rightArr):
                    if leftArr[li] < rightArr[ri]:
                        final.append(leftArr[li])
                        li += 1
                    else:
                        final.append(rightArr[ri])
                        ri += 1
                elif li < len(leftArr):
                    final.append(leftArr[li])
                    li += 1
                elif ri < len(rightArr):
                    final.append(rightArr[ri])
                    ri += 1

            return final
                


        def mergesort(array):
            
            if len(array) <= 1:
                return array
            midpoint = len(array) //2
            sortedLeft = mergesort(array[:midpoint])
            sortedRight = mergesort(array[midpoint:])

            return merge(sortedLeft, sortedRight)


        if len(nums) == 0 or len(nums) == 1:
            return nums
        return mergesort(nums)
