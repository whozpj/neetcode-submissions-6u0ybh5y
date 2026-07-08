class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        


        if len(edges) != n - 1:
            return False

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



            

        seen = set()

        def dfs(node, parent):

            seen.add(node)

            if node in adjacencyList:

                for neighbor in adjacencyList[node]:
                    
                    if neighbor == parent:
                        continue

                    if neighbor in seen:
                        return False

                    if dfs(neighbor, node) == False:
                        return False



        if dfs(0,-1) == False:
            return False

        if len(seen) != n:
            return False

        return True