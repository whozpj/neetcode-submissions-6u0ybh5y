class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        adjacency_map = {}
        seen = set()
        result = 0

        for i, j in edges:
            if i not in adjacency_map:
                adjacency_map[i] = [j]
            else:
                adjacency_map[i].append(j)

            if j not in adjacency_map:
                adjacency_map[j] = [i]
            else:
                adjacency_map[j].append(i)

        
        def dfs(node):
            
            if node in adjacency_map:
                for neighbor in adjacency_map[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        dfs(neighbor)

        for node in range(n):

            if node not in seen:
                seen.add(node)
                dfs(node)
                result += 1

        
        return result
