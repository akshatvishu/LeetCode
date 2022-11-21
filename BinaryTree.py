## Binary Tree

class BinaryTreeNode:
    def __init__(self,data) :
        self.data = data
        self.left_child = None
        self.right_child = None 

def insert(root, newValue) :
    if root is None:
        root = BinaryTreeNode(newValue)
        return root 
    if newValue < root.data:
        root.left_child = insert(root.left_child, newValue)
    else:
        root.right_child = insert (root.right_child, newValue)
    return root 


def height(root):
    if root == None:
        return 0
    height_left_sub_tree = height(root.left_child)
    height_right_sub_tree = height(root.right_child)

    if height_left_sub_tree > height_right_sub_tree:
        return height_left_sub_tree + 1
    else:
        return height_right_sub_tree + 1

def BalancedBTree(root):
    if root == None:
        return True,0
    left_height = height(root.left_child)
    right_height = height(root.right_child)

    if(abs(left_height - right_height)>1):
        return False

    left_sub_tree_balance = BalancedBTree(root.left_child)
    right_sub_tree_balance = BalancedBTree(root.right_child)

    if left_sub_tree_balance and right_sub_tree_balance == True:
        return True
root = insert(None,15)

print(root.data)
root= insert(None,15)
insert(root,10)
insert(root,25)
insert(root,6)
insert(root,14)
insert(root,20)
insert(root,60)

print(height(root))
