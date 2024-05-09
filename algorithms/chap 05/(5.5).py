class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

    def preorder(self):
        if self is not None:
            print(self.data, end='')
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

d = TNode('D', None, None)
e = TNode('E', None, None)
b = TNode('B', d, e)
f = TNode('F', None, None)
c = TNode('C', f, None)
root = TNode('A', b, c)

print('Pre-Order:', end='')
root.preorder()
print()
