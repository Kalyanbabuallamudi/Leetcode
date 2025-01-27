class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Create a 2D boolean matrix to track prerequisites
        is_prerequisite = [[False] * numCourses for _ in range(numCourses)]
        
        # Populate direct prerequisites
        for pre, course in prerequisites:
            is_prerequisite[pre][course] = True
        
        # Floyd-Warshall algorithm to find transitive closure
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if is_prerequisite[i][k] and is_prerequisite[k][j]:
                        is_prerequisite[i][j] = True
        
        # Answer each query based on the matrix
        return [is_prerequisite[u][v] for u, v in queries]


# This code is Contributed by Kalyan Babu Allamudi