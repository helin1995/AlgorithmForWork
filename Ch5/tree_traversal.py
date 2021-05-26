from pythonds.basic.stack import Stack

class TreeNode():
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 构建一颗二叉树
tree = TreeNode(1)
tree.left = TreeNode(2)
tree.right = TreeNode(3)
tree.left.left = TreeNode(4)
tree.left.right = TreeNode(5)
tree.right.left = TreeNode(6)
tree.right.right = TreeNode(7)

def recursiveOrder(res, root):
    # 以递归的方式遍历二叉树
    if root == None:
        return
    # 前序遍历
    # print(root.val)
    # res.append(root.val)
    recursiveOrder(res, root.left)
    # 中序遍历
    # print(root.val)
    # res.append(root.val)
    recursiveOrder(res, root.right)
    # 后序遍历
    # print(root.val)
    res.append(root.val)

def inorder(root):
    # 以非递归的方式遍历二叉树：中序遍历
    if root == None:
        return None
    stack = Stack()
    while root != None:
        stack.push(root)
        root = root.left
    while not stack.isEmpty():
        node = stack.pop()
        print(node.val)
        right = node.right
        while right != None:
            stack.push(right)
            right = right.left

def preorder(root):
    # 以非递归的方式遍历二叉树：前序遍历
    if root == None:
        return None
    stack = Stack()
    stack.push(root)
    while not stack.isEmpty():
        node = stack.pop()
        print(node.val)
        if node.right != None:
            stack.push(node.right)
        if node.left != None:
            stack.push(node.left)

def postorder(root):
    # 以非递归的方式遍历二叉树：后序遍历
    if root == None:
        return None
    stack1 = Stack()
    stack2 = Stack()
    stack1.push(root)
    while not stack1.isEmpty():
        cur = stack1.pop()
        stack2.push(cur)
        if cur.left != None:
            stack1.push(cur.left)
        if cur.right != None:
            stack1.push(cur.right)
    while not stack2.isEmpty():
        print(stack2.pop().val)

res = []
# recursiveOrder(res=res, root=tree)
# inorder(tree)
# preorder(tree)
postorder(tree)
print(res)