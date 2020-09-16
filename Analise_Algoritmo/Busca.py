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



vetor = [0, 10, 20, 30, 40, 50, 60, 70]