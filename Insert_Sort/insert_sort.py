def insert_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i - 1
        while j >= 0 and key < list[j]:
            list[j + 1] = list[j]
            j -= 1
        list[j + 1] = key
        print(list)
    return list


A = [12, 11, 13, 5, 6]
print(f"O vetor A {A} ordenado fica {insert_sort(A)}")