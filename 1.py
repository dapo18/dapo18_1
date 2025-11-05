from collections import deque

class Node:
    def __init__(self, v): self.v, self.l, self.r = v, None, None

def build_tree(values):
    if not values: return None
    nodes = [Node(v) for v in values]
    i = 0
    for j in range(1, len(values), 2):
        if j < len(values): nodes[i].l = nodes[j]
        if j+1 < len(values): nodes[i].r = nodes[j+1]
        i += 1
    return nodes[0]

def preorder(n): return [] if not n else [n.v]+preorder(n.l)+preorder(n.r)
def inorder(n):  return [] if not n else inorder(n.l)+[n.v]+inorder(n.r)
def postorder(n):return [] if not n else postorder(n.l)+postorder(n.r)+[n.v]

vals = input("Введите узлы через пробел: ").split()
root = build_tree(vals)
print("Preorder:", *preorder(root))
print("Inorder:", *inorder(root))
print("Postorder:", *postorder(root))
