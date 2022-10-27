class Hash:
    def __init__(self, size):
        self.size = size
        self.list = [-1] * size
    
    def hashFunction(self, word): #converte palavra para valor inteiro(chave vetor)
        hash = len(word) % self.size
        return hash

    def insert(self, word):
        i = self.hashFunction(word) #posicao do vetor
        if self.list[i] == -1 or self.list[i] == -2:
            self.list[i] = word
        else:
            while(self.list[i] != -1 and self.list[i] != -2):
                i += 1
                if i == self.size:
                    i = 0
            self.list[i] = word

        return self.list[i]
    
    def remove(self, word):
        for i in range(self.size):
            if self.list[i] == word:
                self.list[i] = -2

size = int(input())
hash = Hash(size)

while True:
    num = int(input())
    if num == -1:
        break
    word = input()

    if num == 0:
        hash.insert(word)
    if num == 1:
        hash.remove(word)

for word in hash.list:
    print(word)