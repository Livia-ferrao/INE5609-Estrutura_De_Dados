class LinkedList:
    class Node:
        def __init__(self, val=None, prox=None):
            self.value = val
            self.prox = prox

    def __init__(self):
        self.head = self.Node()

    def insert(self, val, pos):
        i = 0
        pivot = self.head
        while i < pos:
            pivot = pivot.prox
            i += 1
        new_node = self.Node(val)
        new_node.prox = pivot.prox
        pivot.prox = new_node

    def remove(self, pos):
        i = 0
        pivot = self.head
        while i < pos:
            pivot = pivot.prox
            i += 1
        x = pivot.prox
        pivot.prox = pivot.prox.prox
        return x.value

    def is_empty(self):
        return self.head.prox == None

    def __str__(self):
        s = "["
        p = self.head.prox
        while p is not None:
            s += str(p.value) + ", "
            p = p.prox
        s += "]"
        return s

    def iter(self):
        p = self.head.prox
        while p is not None:
            yield p.value
            p = p.prox


class Stack(LinkedList):
    
    def push(self, val):
        self.insert(val, 0)

    def pop(self):
        self.remove(0)

    def top(self):
        return self.head.prox.value

L = LinkedList()
for i in range(10):
    L.insert(10*i, i)
print(L)
print(L.remove(0))
print(L)
print(L.remove(3))
print(L)
print(L.remove(7))
print(L)

#for x in L:
#    print(x)


#S = Stack()
#for i in range(10):
#    S.push(i*10)
#while(not S.is_empty()):
#    print(S.top())
#    S.pop()
