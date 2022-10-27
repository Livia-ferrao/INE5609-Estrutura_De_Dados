class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def remove(self, pointer):
        pointer.next = pointer.next.next

    def append(self, data):
        if self.tail is None:
            node = Node(data)
            self.tail = node
            node.next = self.tail    
        else:
            node = Node(data)
            node.next = self.tail.next
            self.tail.next = node

    def solveJosephus(self, m, n):
        pointer = self.tail.next
        while(n > 1):
            step = 1
            while(step < m):
                pointer = pointer.next
                step +=1
            if m % n != 0:
                #print("Removido: " + str(pointer.next.data))
                self.remove(pointer)
            else:
                pointer = pointer.next
                pointer.next = pointer.next.next
            pointer = pointer.next
            n = n -1
        return str(pointer.data)


qntd = int(input())
for i in range(qntd):
    n = int(input()) #numero de pessoas
    m = int(input()) #passos
    lista = CircularLinkedList()
    for num in range(1, n+1):
        lista.append((n+1)-num)
    resul = lista.solveJosephus(m, n)
    print(f"Usando n={n}, m={m}, resultado={resul}")