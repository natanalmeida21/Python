def bubble_sort(list):
    ordenado = False
    while True:
        ordenado = True
        for i in range(len(list) - 1):
            if list[i] > list [i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                ordenado = False
            print(list)
    return list

a = [30, 50, 10, 35, 70, 45, 80, 100, 22]
bubble_sort(a)