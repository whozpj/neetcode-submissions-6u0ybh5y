class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        seen = set()
        adjacencyList = {}


        for i,j in edges:
            if i in adjacencyList:
                adjacencyList[i].append(j)
            else:
                adjacencyList[i] = [j]
            if j in adjacencyList:
                adjacencyList[j].append(i)
            else:
                adjacencyList[j] = [i]

        result = 0 




        def bfs(node):
            seen.add(node)


            queue = [node]

            while queue:
                nod = queue.pop(0)

                if nod in adjacencyList:
                    for edge in adjacencyList[nod]:
                        if edge not in seen:
                            queue.append(edge)
                            seen.add(edge)

        for node in range(n):
            if node not in seen:
                bfs(node)
                result += 1
        return result
        


        