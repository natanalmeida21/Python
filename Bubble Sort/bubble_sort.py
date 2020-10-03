def bubble_sort(list):
    ordenado = False
    while not ordenado: #Vai verificar se a lista estar ordenada, senão estiver enra no laço de repetição
        ordenado = True
        for i in range(len(list) - 1): #Como no Python começa por zero a posição vai ser o tamanho da lista menos um
            if list[i] > list [i + 1]: #Comparação das posição 
                list[i], list[i + 1] = list[i + 1], list[i] #Se condição acontecer, os números nos indicies vão trocar de lugar
                ordenado = False
            print(list)
    return list

a = [3, 5, 7, 1, 5, 9, 66, -15]
bubble_sort(a)