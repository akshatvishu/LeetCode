# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# O(n) approach! 
def invert(node):
    if node == None:
        return None
    else:
        temp = node
        #Recursive Call
        invert(node.right)
        invert(node.left)
        #Invert
        temp = node.right
        node.right = node.left
        node.left = temp 
        return node
        

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return invert(root)



## A better way to write
# Post-Order
# class Solution:
#     def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
#         if root:
#             invert = self.invertTree
#             root.left,root.right = invert(root.right), invert(root.left)
#             return root 
# Pre-order 
# if not root:
#     return root
# root.left, root.right = root.right, root.left
# self.invertTree(root.left)
# self.invertTree(root.right)
# return root
