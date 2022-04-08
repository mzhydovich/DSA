
def set_parent(child, parent):
    if child is not None:
        child.parent = parent


def keep_parent(v):
    if v is not None:
        set_parent(v.left, v)
        set_parent(v.right, v)


def rotate(child, parent):

    if parent.left == child:
        parent.left, child.right = child.right, parent
    else:
        parent.right, child.left = child.left, parent

    gparent = parent.parent
    if gparent is not None:
        if gparent.left == parent:
            gparent.left = child
        else:
            gparent.right = child

    keep_parent(child)
    keep_parent(parent)
    child.parent = gparent


def splay(v):

    if v.parent is None:
        # if v - root
        return v

    parent = v.parent
    gparent = parent.parent

    if gparent is None:
        # zig(zag)
        rotate(v, v.parent)
        return v
    else:
        if (v == parent.left and parent == gparent.left) or (v == parent.right and parent == gparent.right):
            # zig-zig(zag-zag)
            rotate(parent, gparent)
            rotate(v, parent)
        else:
            # zig-zag(zag-zig)
            rotate(v, parent)
            rotate(v, gparent)

        return splay(v)


def search(root, key):
    v = root
    if v is None:
        return None
    if v.key == key:
        return splay(v)
    if v.key < key and v.right is not None:
        return search(v.right, key)
    if v.key > key and v.left is not None:
        return search(v.left, key)
    return splay(v)


def split(root, key):
    if root is None:
        return None, None
    
    v = search(root, key)
    if v.key == key:
        set_parent(v.left, None)
        set_parent(v.right, None)
        return v.left, v.right
    if v.key < key:
        r, v.right = v.right, None
        set_parent(r, None)
        return v, r
    else:
        l, v.left = v.left, None
        set_parent(l, None)
        return l, v


def merge(left, right):
    if left is None:
        return right
    if right is None:
        return left
    left = search(left, right.key)
    left.right, right.parent = right, left
    return left


class Node:

    def __init__(self, key, parent = None, left = None, right = None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right


class SplayTree:

    def __init__(self, root = None):
        self.root = None


    def inorder_traversal(self, v):
        if v is not None:
            self.inorder_traversal(v.left)
            print(v.key, end=" ")
            self.inorder_traversal(v.right)


    def get_root(self):
        return self.root


    def insert(self, key):
        print(f"\ninsert {key}")
        l, r = split(self.root, key)
        self.root = Node(key, None, l, r)
        keep_parent(self.root)


    def remove(self, key):
        print(f"\nremove {key}")
        new_root = search(self.root, key)
        set_parent(new_root.left, None)
        set_parent(new_root.right, None)
        self.root = merge(new_root.left, new_root.right)



tree = SplayTree()

tree.insert(2)
print("Inorder traversal: ", end="")
tree.inorder_traversal(tree.get_root())
tree.insert(1)
print("Inorder traversal: ", end="")
tree.inorder_traversal(tree.get_root())
tree.insert(3)
print("Inorder traversal: ", end="")
tree.inorder_traversal(tree.get_root())

tree.remove(2)
print("Inorder traversal: ", end="")
tree.inorder_traversal(tree.get_root())
tree.remove(1)
print("Inorder traversal: ", end="")
tree.inorder_traversal(tree.get_root())
tree.remove(3)
print("Inorder traversal: ", end="")
tree.inorder_traversal(tree.get_root())
