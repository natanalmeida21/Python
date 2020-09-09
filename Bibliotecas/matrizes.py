from random import randint
def imprimido_matriz(list, linhas):
    for i in range(linhas):
        print(matriz[i])

matriz = []
for i in range(5): #Número de linhas
    matriz.append( [0] * 5) #Número de colunas

for i in range(5):
    for j in range(5):
        matriz[i][j] = randint(555, 999)

imprimido_matriz(matriz, 5)
print("*" * 30)
print("Matriz de 0 e 1")
print("*" * 30)

for i in range(5):
    for j in range(5):
        if matriz[i][j] % 2 == 0:
            matriz[i][j] = 0
        else:
            matriz[i][j] = 1
imprimido_matriz(matriz, 5)