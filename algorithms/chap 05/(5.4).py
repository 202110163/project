class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def calc_height(root):
    if root is None:
        return 0
    hLeft = calc_height(root.left)
    hRight = calc_height(root.right)
    return max(hLeft, hRight) + 1

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print("트리의 높이 =", calc_height(root))