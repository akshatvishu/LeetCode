# Diamter of a binary Tree:
# The diameter of a binary tree is the length of 
# the longest path between any two nodes in the tree. 
# This path may or may not pass through the root node of the tree.

### Recursive Approach ####
# Calcualte the height of left and right subtree of the root node. 
# Then calculate the diameter of the left and right subtree.
# The diameter of the tree is the maximum of the diameter 
# of the left and right subtree.

# The longest path between any two nodes that goes through the root node, 
# which is equal to the sum of the heights of the left and 
# right subtrees plus one (for the root node itself)

#### Big O: O(n^2) 

### Iterative Approach ####
# Big O: O(n)
# Using DFS to traverse the tree and keep track of the diameter of the tree.
# starting from the root node. T
# he algorithm keeps track of the current path and the maximum diameter seen so far.
#  At each node, it updates the maximum diameter by comparing 
# it to the length of the current path plus the lengths of the left and right subtrees of the node.



from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        
        self.max_diameter = 0
        def longest_path(node):
            if not node:
                return 0
            
            left = longest_path(node.left)
            right = longest_path(node.right)
            self.max_diameter = max(self.max_diameter, left + right)
            # Return the maximum of the longest path through the left and right 
            # subtrees of the current node, plus the current node itself
            return max(left, right) + 1
        
        longest_path(root)
        return self.max_diameter