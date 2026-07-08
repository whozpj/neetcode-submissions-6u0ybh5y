import heapq


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        max_heap = []
        heapq.heapify(max_heap)

        l = 0
        r = k - 1

        for i in range(0, k):
            heapq.heappush(max_heap, ((-nums[i]), i))

        result = []
        
        while r < len(nums):
            while not(l <= max_heap[0][1] <= r):
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0])

            l += 1
            r += 1

            if r < len(nums): heapq.heappush(max_heap, ((-nums[r]), r))
        return result