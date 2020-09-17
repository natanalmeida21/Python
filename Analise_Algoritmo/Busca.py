import time

def busca_binaria(lista, item):
    esquerda, direita = 0, len(lista) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista[meio] == item:
            return meio
        elif lista[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1

def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i

def insert_sort(lista):
    for i in range(1, len(lista)):
        j = i - 1
        while True:
            if j >= 0 and lista[j] > lista[j + 1]:
                chave = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = chave
                j -= 1
            else:
                break
    return lista

vetor = []
print("*" * 16, "Menu", "*" * 16)
print("1- Adicionar Inteiros no vetor\n2- Adicionar Strings no vetor")
while True:
    opcao = int(input("Informe a sua opção: "))
    if opcao == 1:
        elementos = int(input("Informe a quantidade de elementos: "))
        for c in range(elementos):
            vetor.append(int(input(f"Qual o elemento(int) para a posição {c}: ")))
        break
    elif opcao == 2:
        elementos = int(input("Informe a quantidade de elementos: "))
        for c in range(elementos):
            vetor.append(str(input(f"Qual o elemento(str) para a posição {c}: ")))
        break
    else:
        print("Opção inválida")

print(f"Seu vetor é {vetor} e ordenado fica {insert_sort(vetor)}")
print("*" * 16, "Escolha a sua busca", "*" * 16)
print("1- Busca binária\n2- Busca sequencial\n3- Ambos")
