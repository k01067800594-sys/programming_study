class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=TreeNode(10)
root.left=TreeNode(20)
root.right=TreeNode(30)

print("루트", root.data)
print("왼쪽 자식",root.left.data)
print("오른쪽 자식",root.right.data)

#------------------------------

class TreeNode2:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

root=TreeNode2(10)

root.left=TreeNode2(20)
root.right=TreeNode2(30)

root.left.left=TreeNode2(40)
root.left.right=TreeNode2(50)
root.right.left=TreeNode(60)
root.right.right=TreeNode(70)

print("루트", root.data)
print("2단계 자식", root.left.data, root.right.data)
print("3단계 자식", root.left.left.data, root.left.right.data, root.right.left.data, root.right.right.data)

# 전위순회
# 루트-> 왼->오

def preorder(node):
    if node is not None:
        print(node.data, end=" ")
        preorder(node.left)
        preorder(node.right)
print("전위순회")
preorder(root)

# 중위순회:왼->루트->오
def inorder(node):
    inorder(node.left)
    print(node.data, end=" ")
    inorder(node.right)
print("중위순회")
inorder(root)

# 후위순회:왼->오->루트
def postorder(node):
    if node is not None:
        postorder(node.left)
        postorder(node.right)
        print(node.data, end=" ")
print("후위순회")
postorder(root)