# Definition for a binary tree node.
from typing import *


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#### Recursive #####  O(n)
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

        # if p and q is None:
        #     return True
        # if p or q is None:
        #     return False
        # if p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

#### Iterative (BFS) ##### Big O: O(n) #####
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        queue = [(p, q)]
        while queue:
            p, q = queue.pop(0)

            if p and q:
                if p.val != q.val:
                    return False
                queue.append((p.left, q.left))
                queue.append((p.right, q.right))
            elif p or q:
                return False
        return True
#### Iterative (DFS) ##### Big O: O(n) 
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack = [(p,q)]
        while stack :
            p,q = stack.pop()
            if p and q:
                if p.val != q.val:
                    return False
                stack.append((p.left,q.left))
                stack.append((p.right,q.right))
            elif p or q:
                return False
        return True
        

