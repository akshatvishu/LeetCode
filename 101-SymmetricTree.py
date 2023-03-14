#Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Recursive
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        else:
            return self.mirrorCheck(root, root)

    def mirrorCheck(self, left, right):
        
        if left is None and right is None:
            return True
        
        if left is None or right is None:
            return False
        
        if right.val != left.val:
            return False
        
        return (self.mirrorCheck(left.left, right.right) 
                and self.mirrorCheck(left.right, right.left))


    # Iterative:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True 
        
        queue = deque([root.left, root.right])

        while queue:
            
            left, right = queue.popleft(), queue.popleft()
            
            if not left and not right:
                continue
            
            if not left or not right or left.val != right.val:
                return False
            
            queue.extend([left.left, right.right, left.right, right.left])
        
        return True
    
    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True 
        
        stack =([root.left, root.right])

        while stack:

            left, right = stack.pop()

            if left is None and right is None:
                continue

            if left is None or right is None or left.val != right.val:
                return False
            stack.extend([left.left, right.right, left.right, right.left])
            # stack.append([left.left, right.right])
            # stack.append([left.right, right.left])
        
        return True
            

        
        
        
