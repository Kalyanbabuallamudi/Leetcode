# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        def min_swaps_to_sort(arr):
            n = len(arr)
            indexed_arr = [(val, idx) for idx, val in enumerate(arr)]
            indexed_arr.sort()  # Sort by value
            visited = [False] * n
            swaps = 0

            for i in range(n):
                if visited[i] or indexed_arr[i][1] == i:
                    continue

                cycle_length = 0
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = indexed_arr[j][1]
                    cycle_length += 1

                if cycle_length > 1:
                    swaps += cycle_length - 1

            return swaps

        if not root:
            return 0

        queue = deque([root])
        total_operations = 0

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            total_operations += min_swaps_to_sort(current_level)

        return total_operations

# This Code is Contributed by Kalyan Babu Allamudi