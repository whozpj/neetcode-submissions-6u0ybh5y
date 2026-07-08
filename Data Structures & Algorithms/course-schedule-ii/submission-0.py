class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        




        adjacencyList = {}

        for i,j in prerequisites:

            if i in adjacencyList:
                adjacencyList[i].append(j)
            else:
                adjacencyList[i] = [j]


        visiting = set()
        visited = set()

        path = []

        def dfs(node):

            if node in visiting:
                return False
            if node in visited:
                return True

            visiting.add(node)
            
            if node in adjacencyList:
                for neighbor in adjacencyList[node]:

                    if dfs(neighbor) == False: return False

            path.append(node)
            visiting.remove(node)
            visited.add(node)
            return True

        for i in range(numCourses):
            if i not in visiting:
                if dfs(i) == False:
                    return []
        return path

