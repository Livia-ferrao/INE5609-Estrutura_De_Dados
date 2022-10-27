class Node:
    def __init__(self, value=None, _next=None, _prev=None):
        self._value = value
        self._next = _next
        self._prev = _prev


class DoubleLinkedList:

    def __init__(self):
        self._head = Node("Head")        
        self._tail = Node("Tail")
        self._head._next = self._tail
        self._tail._prev = self._head

    def insert(self, val, pos):
        new_node = Node(value=val)
        pivot = self._head
        idx = 0
        while idx < pos:
            pivot = pivot._next
            idx += 1
        new_node._next = pivot._next
        new_node._prev = pivot
        pivot._next = new_node
        new_node._next._prev = new_node

    def print_reversed(self):
        tostr = "["
        pivot = self._tail._prev
        while pivot != self._head:
            tostr += str(pivot._value) + ", "
            pivot = pivot._prev
        tostr += "]"
        print(tostr)

    def __str__(self):
        tostr = "["
        pivot = self._head._next
        while (pivot != self._tail):
            tostr += str(pivot._value) + ", "
            pivot = pivot._next
        tostr += "]"
        return tostr

    def is_empty(self):
        return self._head._next == None


if __name__ == "__main__":
    L = DoubleLinkedList()
    for i in range(10):
        L.insert(i, i)
    print(L)
    L.print_reversed()
