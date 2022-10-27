class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BinaryTree:
    def __init__(self):
        self.root = None
        self.order = ['-', '+', '*', '/']

    def build_tree(self, expressao):
        lista = []
        for signal in self.order:
            for value in expressao[::-1]:
                if value == signal:
                    if len(lista) != 0:        #diferente de vazio
                        i = expressao[0:lista[len(lista)-1]+1].rindex(value)
                    else:
                        i = expressao.rindex(value)
                    lista.append(i)
                    root = expressao[i]
                    root = expressao[i]
                    left = expressao[0:i]
                    right = expressao[i+1:]
                    return root, left, right
        return expressao[0]


    def build_nodes(self, expressao, tree):
        if len(expressao) > 2:
            value, left, right = self.build_tree(expressao)

            value_l = self.build_tree(left)
            value_l = value_l[0]

            value_r = self.build_tree(right)
            value_r = value_r[0]

            if self.root == None:
                self.root = Node(value)
                tree = self.root
            
            tree.left = Node(value_l)
            tree.right = Node(value_r)
            self.build_nodes(left, tree.left)
            self.build_nodes(right, tree.right)

    def pos_order(self, root):
        if root != None:
            l_child = root.left
            r_child = root.right

            self.pos_order(l_child)
            self.pos_order(r_child)
            print(root.value, end="")
    
    def pre_order(self, root):
        if root != None:
            l_child = root.left
            r_child = root.right

            print(root.value, end="")
            self.pre_order(l_child)
            self.pre_order(r_child)


b_tree = BinaryTree()
expressao = input()
b_tree.build_nodes(expressao, b_tree.root)
b_tree.pre_order(b_tree.root)
print()
b_tree.pos_order(b_tree.root)