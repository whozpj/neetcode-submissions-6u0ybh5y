class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        intervals.sort()
        indexed_queries = sorted((q, i) for i, q in enumerate(queries))

        ans = [-1] * len(queries)
        heap = []
        j = 0

        for q, idx in indexed_queries:
            while j < len(intervals) and intervals[j][0] <= q:
                left, right = intervals[j]
                length = right - left + 1
                heapq.heappush(heap, (length, right))
                j += 1

            while heap and heap[0][1] < q:
                heapq.heappop(heap)

            if heap:
                ans[idx] = heap[0][0]

        return ans