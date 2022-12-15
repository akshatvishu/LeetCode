from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        level = 0
        queue = deque([(root, 1)])
        while queue:
            # BFS Traversal
            node, level = queue.popleft()
            print(f'node: {node}, level: {level}')
            if not node.left and not node.right: # means we reached a leaf node hence we return the lvl
                return level 
            #If it is not a leaf node, we add the left and right children to the queue(repeating it till we get leaf node). 
            # The level for the children is level+1.
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
