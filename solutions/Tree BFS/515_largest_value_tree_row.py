from typing import Optional, List
from collections import deque

# Defination of a binary tree node
class TreeNode:
    def __init__ (slef, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        largest_values = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            max_value = float("-inf")

            for _ in range (level_size):
                node = queue.popleft()
                max_value = max(max_value, node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            largest_values.append(max_value)
        
        return largest_values

# This Code is Contributed by Kalyan Babu Allamudi