import math
def insercao(a, b):
    x = ((a ** 2) * 2) / b
    return x

def intercalacao(a, b):
    x = ((math.log10(a)) * a) / b

n = int(input("Quantos elementos serão ordenados? "))
m = int(input("Quantas instruções por segundo? "))
a = int(input("Escolha um opção: 1- Inserção 2- Intercalação 3- Ambos"))
if a == 1:
    print(f"O resultado por inserção é {insercao(n, m)}")
elif a == 2:
    print(f"O resultado por intercalação é {intercalacao(n, m)}")
elif a == 3:
    print(f"I resulto por inserção é {insercao(n, m)} e por intercalação é {intercalacao(n, m)}")
else:
    print("Essa opção é inválida")