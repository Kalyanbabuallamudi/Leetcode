class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Helper function to find the root of a node
        def find(parent, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])  # Path compression
            return parent[node]
        
        # Helper function to union two nodes
        def union(parent, rank, node1, node2):
            root1 = find(parent, node1)
            root2 = find(parent, node2)
            
            if root1 != root2:
                if rank[root1] > rank[root2]:
                    parent[root2] = root1
                elif rank[root1] < rank[root2]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    rank[root1] += 1
        
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)
        
        for u, v in edges:
            if find(parent, u) == find(parent, v):
                return [u, v]  # This edge creates a cycle
            else:
                union(parent, rank, u, v)


# This code is contributed by Kalyan Babu Allamudi