class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# class Solution:
#     def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
#         # list to hold the stack
#         stack = []
#         # left will hold the left subtree of the current node
#         left = None

#         # iterate through the array
#         for num in nums:
#             # create a new node
#             node = TreeNode(num)
#             # Now, we check is stack is not empty and current element
#             # is greater than the top element of the stack
#             # if yes, then we pop the node and connect to the right of
#             # current node
#             while stack and stack[-1].val < num:
#                 left = stack.pop()
#                 node.left = left

#             if stack:
#                 # If stack is not empty
#                 # Current element is less than the top element in stack
#                 # so conenct the curr node in the right of the top element
#                 # node in stack
#                 stack[-1].right = node
#             stack.append(node)  # add current node in the stack

#         return stack[0]  # Most bottom element in the stack

# O(n)
def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
	stack = []

	for x in nums:
		n = TreeNode(x)
		# if stack[-1] is less than x, then pop stack[-1] and set n.left to it
		while stack and x > stack[-1].val:
			n.left = stack.pop()

		# if stack[-1] is greater than x, then set n to stack[-1].right
		if stack:
			stack[-1].right = n               
		stack.append(n)

	return stack[0]

# x = Solution()
# x.constructMaximumBinaryTree(nums=[1,2,3,0,7,4])
#https://leetcode.com/problems/maximum-binary-tree/solutions/106146/C++-O(N)-solution/