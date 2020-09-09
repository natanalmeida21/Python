import math
def insercao(a, b):
    x = ((a ** 2) * 2) / b
    return x

def intercalacao(a, b):
    x = ((math.log10(a)) * a) / b

n = int(input("Quantos elementos serão ordenados? "))
m = int(input("Quantas instruções por segundo? "))
print(f"O resuldado por inserção é {insercao(n,m)}")