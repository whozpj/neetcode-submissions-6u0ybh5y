class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        

        #keep track of a maxheap of size k, use the difference as the deciding factor
        
        heap = []

        for num in arr:
            diff = abs(x-num)
            heapq.heappush(heap, (-diff, -num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []

        while heap:
            diff, num = heapq.heappop(heap)
            result.append(-num)

        result.sort()
        return result



