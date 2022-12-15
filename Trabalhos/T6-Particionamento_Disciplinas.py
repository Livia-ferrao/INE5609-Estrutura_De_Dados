class Queue:
    def __init__(self, max_size):
        self.__items = [None]*(max_size + 1)
        self.__first = 0
        self.__last = 0

    def is_empty(self):
        return self.__first == self.__last

    def push(self, item):
        self.__items[self.__last] = item
        self.__last = (self.__last + 1) % len(self.__items)

    def pop(self):
        item = self.__items[self.__first]
        self.__first = (self.__first + 1) % len(self.__items)
        return item


def get_distances(A, x):
    n = len(A)
    dist = [-1]*n
    q = Queue(n)
    dist[x] = 0
    q.push(x)
    while(not q.is_empty()):
        y = q.pop()
        for i in range(n):
            if A[y][i] == 1 and dist[i] == -1:
                dist[i] = dist[y] + 1
                q.push(i)
    return dist

A = []
n = int(input())
for i in range (0, n):
    linha = []
    for j in range(0, n):
        linha.append(0)
    A.append(linha)
    

while True:
    u, v = input().split(",")
    u, v = int(u), int(v)
    if u == -1 and v == -1:
        break
    A[u - 1][v - 1] = 1
print(A)


start_node = 0
dist = get_distances(A, start_node)
print(max(dist) + 1)
