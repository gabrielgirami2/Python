'''
Faça um programa que leia uma matriz 3x3 de inteiros e multiplique
os elementos da diagonal principal da matriz por um número k.
Imprima a matriz na tela antes e depois da multiplicação .
'''




matriz = []

for l in range(3):
    linha = []
    for col in range(3):
        linha.append(int(input("Digite um numero da matriz: ")))
    matriz.append(linha)

for l in range(3):
    print(matriz[l])

k = int(input("Digite o valor de k: "))

for l in range(3):
    for col in range(3):
        if l == col:
            matriz[l][col]*=k

for l in range(3):
    print(matriz[l])
