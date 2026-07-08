class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #create adjacency list
        adjacencyList = {}
        for i in range(numCourses):
            adjacencyList[i] = []

        #populate the list:
        for course, prereq in prerequisites:
            adjacencyList[course].append(prereq)
        
        #todo

        seen = set()
        def dfs(course):
            if course in seen:
                return False
            
            seen.add(course)

            for courses in adjacencyList[course]:
                if dfs(courses) == False:
                    seen.remove(course)
                    return False
            seen.remove(course)
            adjacencyList[course] = []
            return True


        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True