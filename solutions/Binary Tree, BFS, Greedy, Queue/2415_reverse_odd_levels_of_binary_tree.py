from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root])  # Use a queue to perform level-order traversal
        level = 0  # Keep track of the current level (root is level 0)
        
        while queue:
            level_size = len(queue)  # Number of nodes at the current level
            level_nodes = []  # To store node references at the current level
            
            for _ in range(level_size):
                node = queue.popleft()
                level_nodes.append(node)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            if level % 2 == 1:  # Reverse values at odd levels
                values = [node.val for node in level_nodes][::-1]
                for i, node in enumerate(level_nodes):
                    node.val = values[i]
            
            level += 1  # Move to the next level
        
        return root

# This Code is Contributed by Kalyan Babu Allamudi