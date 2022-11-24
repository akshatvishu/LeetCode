## Binary Tree
from typing import *

class BinaryTreeNode:
    def __init__(self,data) :
        self.data = data
        self.left_child = None
        self.right_child = None 

## O(n) -> no of nodes in the tree and we have to do this opertation n times thus, O(n^2)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

## O(n^2)##
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None: 
            return True
        left = self.height(root.left)
        right = self.height(root.right)
        if(abs(left - right)>1):
            return False
        
        return (self.isBalanced(root.left) and self.isBalanced(root.right))

    def height(self,root):
        if root == None :
            return 0

        left_height = self.height(root.right)
        right_height = self.height(root.left)

        return max(left_height,right_height)+1

##Worst case (if tree is completely imbalanced), the space complexity would be O(N). Worst-case time complexity of O(N)/space-complexity is O(max height of tree
#  DFS the tree and recursively check if each subtree is balanced -> O(N)
def check(node):
    if node == None:
        return(0,True)
    
    l_height, l_balanced = check(node.left)
    r_height, r_balanced = check(node.right)
    return max(l_height + r_height)+1, l_balanced and r_balanced and abs(l_height - r_height) <=1 

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return check(root)[0]