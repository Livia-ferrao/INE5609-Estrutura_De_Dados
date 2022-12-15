def BubbleSort(v):
    swapped = True
    count = 0
    while swapped:
        swapped = False
        for i in range(1, num):
            if v[i - 1] > v[i]:
                v[i - 1], v[i] = v[i], v[i - 1]
                count += 1
                swapped = True

    return count

num = int(input())
lista = input().split()
for i in range(num):
    lista[i] = int(lista[i])

sort_list = BubbleSort(lista)
print(sort_list)