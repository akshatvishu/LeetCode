from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Using BFS 
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = [root]
        max_val = []

        while queue:
            curr_max = -float('inf')

            for _ in range(len(queue)):
                node = queue.pop(0)

                curr_max = max(node.val,curr_max)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            max_val.append(curr_max)
        return(max_val)


# Using DFS:

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.max_val = []
        if root is None: # empty tree
            return []
        self.dfs(root,0) # start at level 0
        return self.max_val 
    def dfs(self, node, level):
        if node is None: # leaf node
            return
        if level == len(self.max_val): # if we are at a new level
            self.max_val.append(node.val) # add the value to the list
        else:
            self.max_val[level] = max(self.max_val[level], node.val) # update the max value at the current level
        self.dfs(node.left, level+1)
        self.dfs(node.right, level+1)


        
# we use a helper function dfs that performs the DFS 
# and keeps track of the current depth level. 
# As we visit each node, 
# we check if the current depth level is equal to the size of the `max_val` list. 
# If it is, we add the value of the current node to the max_val list. 
# Otherwise, we update the value at the current depth level to be the maximum 
# of the current value and the value of the current node.
            


        
            