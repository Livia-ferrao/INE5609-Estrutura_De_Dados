class Queue:
    def __init__(self):
        self.queue = [None] * 1000000
        self.head = 0
        self.last = 0

    def insert(self, item):
        self.queue[self.last] = item
        self.last += 1

    def pop(self):
        x = self.queue[self.head]
        self.head += 1
        return x

    def empty(self):
        return self.last == self.head


def acha_menor_caminho(origem, destino):  #[0,0,0]  [1,1,0]
    q = Queue()
    q.insert(origem)    #q = (  [0,0,0]  )
    testados = [[False]*8 for i in range(8)]

    while not q.empty():
        posi_pop = q.pop()  #  [0,0,0] 
        
        if posi_pop[1] == destino[1] and posi_pop[0] == destino[0]:
            return posi_pop[2]   #retorna passos

        prox_posicoes = []  # [ [2,1,0], [2,3,0] ...  ]

        for movimento in [[-1,-2],[-2,-1],[-2,1],[-1,2],[1,2],[2,1],[2,-1],[1,-2]]:
            prox_posicoes.append([posi_pop[0]+movimento[0], posi_pop[1]+movimento[1], posi_pop[2]])

        for position in prox_posicoes:
            x = position[0]
            y = position[1]
            step = position[2]

            if (0 <= x < 8) and (0 <= y < 8) and not testados[x][y]:
                q.insert([x, y, step+1])
                testados[x][y] == True
                

init = input()
end = input()

num = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
linha_init = num.index(init[0])
linha_end = num.index(end[0])

inicio = [linha_init, int(init[1]) - 1, 0]
fim = [linha_end, int(end[1]) - 1, 0]

steps = acha_menor_caminho(inicio, fim)

print("Movimentos: %d" % steps)