import math
n = int(input("Quantos elementos serão ordenados? "))
m = int(input("Quantas instruções por segundo? "))
insercao = ((n ** 2) * 2) / m
intercalacao = ((math.log10(n)) * n) / m
print(insercao)