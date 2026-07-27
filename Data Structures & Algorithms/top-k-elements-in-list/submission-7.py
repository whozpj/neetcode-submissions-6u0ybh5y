class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        arr = [[] for _ in range(len(nums)+1)]

        counts = {}

        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1


        for num in counts:
            arr[counts[num]].append(num)
        result = []
        for i in range(len(arr)-1,-1,-1):
            if arr[i] != []:
                for num in arr[i]:
                    result.append(num)
                    if len(result) == k:
                        return result
