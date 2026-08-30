class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        

        adjacencyList = {}
        for course, prereq in prerequisites:
            if course in adjacencyList:
                adjacencyList[course].append(prereq)
            else:
                adjacencyList[course] = [prereq]

        visiting = set()
        visited = set()

        def dfs(node):

            if node in visited:
                return True

            if node in visiting:
                return False

            visiting.add(node)

            if node in adjacencyList:
                for neighbor in adjacencyList[node]:
                    if dfs(neighbor) == False:
                        return False

            visiting.remove(node)
            visited.add(node)
            return True

        for i in range(numCourses):
            if i not in visited:
                if dfs(i) == False:
                    return False


        return True




        