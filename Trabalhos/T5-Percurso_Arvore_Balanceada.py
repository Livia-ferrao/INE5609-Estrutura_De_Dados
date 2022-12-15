class Node():
    def __init__(self, elem):
        self.elem = elem
        self.left = None
        self.right = None
        self.height = 1

class AVL():
    def insert(self, root, elem):
        if not root:
            return Node(elem)
        elif elem < root.elem:
            root.left = self.insert(root.left, elem)
        else:
            root.right = self.insert(root.right, elem)

        root.height = self.executeHeight(root)
        balanceFactor = self.balance(root)
        value = self.executeBalance(balanceFactor, root, elem)
        return value

    def executeBalance(self, balance, root, elem):
        if balance > 1:
            if elem<root.left.elem:
                return self.rightRotate(root)
            else:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

        if balance < -1:
            if elem>root.right.elem:
                return self.leftRotate(root)
            else:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        raiz = root
        return raiz

    def executeHeight(self, root):
        height_node = 1 + max(self.height(root.left),
                              self.height(root.right))
        return height_node

    def rightRotate(self, z):
        y = z.left
        tree = y.right
        y.right = z
        z.left = tree
        z.height = 1 + max(self.height(z.left),
                           self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))
        element = y
        return element
    
    def leftRotate(self, z):
        y = z.right
        tree = y.left
        y.left = z
        z.right = tree
        z.height = 1 + max(self.height(z.left),
                           self.height(z.right))
        y.height = 1 + max(self.height(y.left),
                           self.height(y.right))
        element = y
        return element


    def height(self, root):
        if root:
            get_height = root.height
        else:
            return 0
        height = get_height
        return height

    def balance(self, root):
        if root:
            get_balance = (self.height(root.left) - self.height(root.right))
        else:
            return 0
        balance = get_balance
        return balance

    def em_ordem(self, root):
        if root != None:
            self.em_ordem(root.left)
            if root.elem != None:
                print(root.elem, end=" ")
            self.em_ordem(root.right)

    def pre_ordem(self, root):
        if root != None:
            if root.elem != None:
                print(root.elem, end=" ")
            self.pre_ordem(root.left)
            self.pre_ordem(root.right)

    def pos_ordem(self, root):
        if root != None:
            self.pos_ordem(root.left)
            self.pos_ordem(root.right)
            if root.elem != None:
                print(root.elem, end=" ")

tree_avl = AVL()
num = int(input())
root = None
for i in range(num):
    elem = int(input())
    root = tree_avl.insert(root, elem)

tree_avl.pre_ordem(root)
print()
tree_avl.em_ordem(root)
print()
tree_avl.pos_ordem(root)