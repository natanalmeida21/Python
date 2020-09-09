def bubble_sort(list):
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(len(list) - 1):
            if list[i] > list [i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                ordenado = False
            print(list)
    return list

a = [3, 5, 7, 1, 5, 9]
bubble_sort(a)