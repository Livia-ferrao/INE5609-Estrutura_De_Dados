class Node:

    def __init__(self, val):
        self.value = val
        self.left = None
        self.right = None
        
class Tree:

    def __init__(self):
        self.root = None

    def search(self, pivot, k):
        if k == pivot.value:
            return pivot
        else:
            if k <= pivot.value:
                if pivot.left is not None:
                    return self.search(pivot.left, k)
            else:
                if pivot.right is not None:
                    return self.search(pivot.right, k)
        return pivot

    def insert(self, val):
        new_node = Node(val)    
        if self.root is None:
            self.root = new_node
        else:
            # Assumindo que não tem elementos repetidos:
            pivot = self.search(self.root, val)
            if val <= pivot.value:
                pivot.left = new_node 
            else:
                pivot.right = new_node

    def inorder(self, pivot):
        if (pivot is not None):
            self.inorder(pivot.left)
            print(pivot.value)
            self.inorder(pivot.right)

tree = Tree()
tree.insert(50)
tree.insert(30)
tree.insert(76)
tree.insert(20)
tree.insert(45)
tree.insert(58)
tree.insert(98)
tree.insert(1)
tree.insert(27)
tree.inorder(tree.root)

