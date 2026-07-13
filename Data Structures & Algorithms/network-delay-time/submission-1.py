class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        


        adjacencyList = {}
        result = 0
        seen = set()
        minHeap = [(0,k)]




        for source, target, time in times:

            if source in adjacencyList:
                adjacencyList[source].append((target, time))
            else:
                adjacencyList[source] = [(target, time)]

        while minHeap:

            currTime, node = heapq.heappop(minHeap)

            if node not in seen:
                seen.add(node)
                result = max(result, currTime)

                if node in adjacencyList:
                    for neighbors, weight in adjacencyList[node]:
                        heapq.heappush(minHeap, (currTime + weight, neighbors))

        if len(seen) == n:
            return result
        else:
            return -1

        