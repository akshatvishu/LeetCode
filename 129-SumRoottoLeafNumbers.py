from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# We need to transverse the tree -> BFS(dequeue) or DFS(recursion / stack)

def bfs(root):
        if not root:
            return 0
        
        queue = deque([(root, 0)])
        total_sum = 0

        while queue:
            node, current_num = queue.popleft()
            current_num = current_num * 10 + node.val

            if not node.left and not node.right:
                total_sum += current_num
            
            else:            
                if node.left:
                    queue.append((node.left, current_num))
                
                if node.right:
                    queue.append((node.right, current_num))

        return total_sum
root = [1, 2, 3]
if not root:
    print(0)

queue = deque([(root, 0)])
print(queue)
total_sum = 0

# while queue:
#     node, current_num = queue.popleft()
#     current_num = current_num * 10 + node.val

#     if not node.left and not node.right:
#         total_sum += current_num
            